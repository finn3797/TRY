import config from "@/config"
import http from "@/utils/request"

export default {
	token: {
		url: `${config.API_URL}/auth`,
		name: "登录获取TOKEN",
		post: async function(data={}){
			return await http.post(this.url, data);
		}
	},
	info: {
		url: `${config.API_URL}/me`,
		name: "获取登录用户信息",
		post: async function(data={}){
			return await http.post(this.url);
		}
	}
}
