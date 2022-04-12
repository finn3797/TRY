<template>
  <el-container>
    <el-header>
      <div class="left-panel">
        <el-button type="primary" icon="el-icon-plus" @click="add"></el-button>
        <!-- <el-button
          v-if="selection.length > 0"
          type="danger"
          plain
          icon="el-icon-delete"
        ></el-button> -->
      </div>
      <div class="right-panel">
        <div class="right-panel-search">
          <scFilterBar :options="options" @change="change"></scFilterBar>
        </div>
      </div>
    </el-header>
    <el-main class="nopadding">
      <scTable
        tableName="templateList"
        ref="table"
        :data="list"
        :column="column"
        stripe
      >
      </scTable>
    </el-main>
  </el-container>
</template>
<script>
export default {
  name: "SpForm",
  data() {
    return {
      options: [
        {
          label: "名称",
          value: "name",
          type: "text",
        },
        {
          label: "类型",
          value: "type",
          type: "select",
          extend: {
            multiple: true,
            data: [
              {
                label: "数据",
                value: "1",
              },
              {
                label: "表单",
                value: "2",
              },
            ],
          },
        },
        {
          label: "创建时间",
          value: "date",
          type: "daterange",
        },
      ],
      column: [
        {
          label: "ID",
          prop: "id",
          width: "100",
          sortable: true,
          hide: true,
        },
        {
          label: "名称",
          prop: "name",
          width: "300",
        },
        {
          label: "状态",
          prop: "state",
          width: "100",
          filters: [
            { text: "正常", value: "1" },
            { text: "异常", value: "2" },
          ],
        },
        {
          label: "类型",
          prop: "type",
          width: "100",
          filters: [
            { text: "数据", value: "数据" },
            { text: "表单", value: "表单" },
          ],
        },
        {
          label: "负责人",
          prop: "user",
          width: "100",
        },
        {
          label: "进度",
          prop: "progress",
          width: "250",
        },
        {
          label: "创建时间",
          prop: "time",
          width: "150",
          sortable: true,
        },
      ],
      group: "0",
      selection: [],
      list: [],
      info: false,
    };
  },
  methods: {},
};
</script>
