from masonite.notification import Notification
from masonite.mail import Mailable
from masonite.utils.collections import collect


class Notice(Notification, Mailable):
    def to_mail(self, notifiable):
        return (
            self.to(notifiable.email)
            .subject("Masonite 4")
            .from_("hello@email.com")
            .text(f"Hello {notifiable.name}")
        )

    def to_database(self, notifiable):
        return {"data": notifiable.ext}

    def via(self, notifiable):
        return ["database"]
