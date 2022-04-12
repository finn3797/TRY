<template>】
<sc-form ref="formref" :config="config" v-model="form" :loading="loading">
	<el-button type="primary" @click="save">保 存</el-button>
	<el-button @click="reset">重 置</el-button>
</sc-form>
</template>
<script>
	export default {
		name: 'SpForm',
		data(){
			return {
				loading: false,
				config: {},
				form: {}
			}
		},
		mounted() {
			//模拟请求延迟, 配置参数和form值并无顺序要求，可同时请求
			const config = {
				labelWidth: '130px',
				labelPosition: 'right',
				size: 'medium',
				formItems: [
					{
						label: "ElementPlus",
						component: "title",
					},
					{
						label: "输入框",
						name: "name",
						value: "",
						component: "input",
						options: {
							maxlength: "20",
							placeholder: "Activity name",
						},
						rules: [
							{required: true, message: "Please input Activity name", trigger: "blur"}
						],
						requiredHandle: "$.required==true",
					},
					{
						label: "栅格(12/24)",
						name: "name2",
						value: "",
						component: "input",
						span: 12,
						options: {
							placeholder: "span: 12",
						}
					},
					{
						label: "栅格(12/24)",
						name: "name3",
						value: "",
						component: "input",
						span: 12,
						options: {
							placeholder: "span: 12",
						}
					},
					{
						label: "选择器(多选)",
						name: "select",
						value: "",
						component: "select",
						span: 24,
						options: {
							remote: {
								// api: `${this.$CONFIG.API_URL}/system/dic/get`,
								data: {name: 'a'}
							},
							multiple: true,
							items:[
								{
									label: "选项1",
									value: "1"
								},
								{
									label: "选项2",
									value: "2"
								}
							]
						},
						rules: [
							{required: true, message: "Please input Activity name", trigger: "change"}
						],
						requiredHandle: "$.required==true",
					},
					{
						label: "选择器(单选)",
						name: "select2",
						value: "",
						component: "select",
						span: 24,
						options: {
							remote: {
								// api: `${this.$CONFIG.API_URL}/system/dic/get`,
								data: {name: 'b'}
							},
							items:[
								{
									label: "选项1",
									value: "1"
								},
								{
									label: "选项2",
									value: "2"
								}
							]
						}
					},
					{
						label: "级联选择器",
						name: "cascader",
						value: "",
						component: "cascader",
						span: 24,
						options: {
							items:[
								{
									label: "Guide",
									value: "guide",
									children: [
										{
											label: "Disciplines",
											value: "disciplines"
										},
										{
											label: "Consistency",
											value: "consistency"
										},
									]
								},
								{
									label: "Resource",
									value: "resource",
									children: [
										{
											label: "Axure Components",
											value: "axure"
										},
										{
											label: "Sketch Templates",
											value: "sketch"
										},
										{
											label: "Design Documentation",
											value: "docs"
										}
									]
								},
								{
									label: "Component",
									value: "component"
								},
							]
						}
					},
					{
						label: "多选框",
						name: "checkbox",
						component: "checkbox",
						span: 24,
						tips: "多选框配置加上 name 表示拥有嵌套关系。否则将值“平铺”在form对象",
						options: {
							items:[
								{
									label: "选项1",
									name: "option1",
									value: false
								},
								{
									label: "选项2",
									name: "option2",
									value: false
								}
							]
						},
						hideHandle: "$.required==true"
					},
					{
						label: "多选框组",
						name: "checkboxGroup",
						value: [],
						component: "checkboxGroup",
						span: 24,
						options: {
							items:[
								{
									label: "选项1",
									value: "option1"
								},
								{
									label: "选项2",
									value: "option2"
								}
							]
						},
						hideHandle: "$.required==true"
					},
					{
						label: "单选",
						name: "radio",
						value: "1",
						component: "radio",
						options: {
							items:[
								{
									label: "选项1",
									value: "1"
								},
								{
									label: "选项2",
									value: "2"
								}
							]
						},
						hideHandle: "$.required==true"
					},
					{
						label: "开关",
						name: "required",
						message: "演示如何使用表达式动态显隐和必填，试试打开和关闭开关",
						value: false,
						component: "switch",
					},
					{
						label: "日期/时间",
						name: "date",
						value: "",
						component: "date",
						options: {
							type: "datetime",
							valueFormat: "YYYY-MM-DD HH:mm:ss",
						},
						rules: [
							{required: true, message: "Please input Data", trigger: "change"}
						],
					},
					{
						label: "滑块",
						name: "slider",
						value: 0,
						component: "slider",
						options: {
							marks: {
								0: '0°C',
								8: '8°C',
								37: '37°C'
							}
						}
					},
					{
						label: "数值",
						name: "number",
						value: 0,
						component: "number",
					},
					{
						label: "颜色",
						name: "color",
						value: "",
						component: "color",
					},
					{
						label: "评分",
						name: "rate",
						value: 0,
						component: "rate",
					},
					{
						label: "SCUI扩展",
						component: "title",
					},
					// {
					// 	label: "表格选择器", r
					// 	name: "tableselect",
					// 	value: {},
					// 	component: "tableselect",
					// 	span: 24,
					// 	options: {
					// 		apiObj: '$API.demo.page',
					// 		column: [
					// 			{
					// 				label: "ID",
					// 				prop: "id",
					// 				width:150
					// 			},
					// 			{
					// 				label: "姓名",
					// 				prop: "user"
					// 			}
					// 		],
					// 		props: {
					// 			label: 'user',
					// 			value: 'id',
					// 			keyword: "keyword"
					// 		}
					// 	}
					// },
					{
						label: "上传",
						component: "upload",
						options: {
							items:[
								{
									label: "图像1",
									name: "img1",
									value: ""
								},
								{
									label: "图像2",
									name: "img2",
									value: ""
								}
							]
						}
					},
					{
						label: "富文本",
						name: "text",
						value: "",
						component: "editor",
					},
				]
			}

			const form = {
				name: "Activity name",
				checkbox: {
					option1: true
				},
				checkboxGroup: ["option1"],
				select: ["1"],
				select2: "1",
				cascader: ['resource','docs'],
				tableselect: {
					user: "何敏",
					id: "360000197302144442"
				},
				text: "<p><span style=\"font-size: 28px;\">Editor</span></p>\n<table style=\"border-collapse: collapse; width: 100%;\" border=\"1\">\n<tbody>\n<tr>\n<td style=\"width: 47.4544%; background-color: #ecf0f1;\">Name</td>\n<td style=\"width: 47.4544%;\">SCUI</td>\n</tr>\n<tr>\n<td style=\"width: 47.4544%; background-color: #ecf0f1;\">Describe</td>\n<td style=\"width: 47.4544%;\">Super color UI Admin</td>\n</tr>\n</tbody>\n</table>"
			}

			setTimeout(()=>{
				this.config = config
			},500)

			this.loading = true
			setTimeout(()=>{
				this.form = form
				this.loading = false
			},100)
		},
		methods: {
			submitForm(){
				this.$refs.ruleForm.validate((valid) => {
					if (valid) {
						alert('请看控制台输出');
						console.log(this.form);
					}else{
						return false;
					}
				})
			},
			resetForm(){
				this.$refs.ruleForm.resetFields();
			}
		}
	}
</script>
