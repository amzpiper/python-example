class Test():
    def __init__(self):
        self.table_name = "dm_property_service_satisfy,dm_security_customer_month,dm_security_customer_reform_month,dm_security_complete,dm_energy_overview,dm_energy_water_month,dm_energy_electric_month,dm_energy_heat_month,dm_energy_water_distribution,dm_energy_electric_distribution,dm_operation_overview,dm_operation_alarm,dm_operation_handle,dm_operation_maintenance_month,dm_comprehensive_overview,dm_comprehensive_special_month,dm_comprehensive_access,dm_whole_overview,dm_whole_arm_statisfied_years,dm_whole_arm_statisfied_pro_ranking,dm_whole_operate,dm_branch_overview,dm_branch_arm_statisfied_years,dm_branch_arm_statisfied_ranking,dm_branch_operate,dm_arm_overview,dm_arm_statisfied_years,dm_arm_statisfied_ranking,dm_arm_read_ranking,dm_arm_energy,dm_arm_inspect_type,dm_arm_inspect_sum,dm_arm_inspect_ranking,dm_arm_project_overview,dm_arm_project_statisfied,dm_arm_project_energy,dm_operate_overview,dm_operate_rent,dm_operate_service,dm_operate_service_company,dm_operate_service_live,dm_operate_park,dm_operate_park_income_month,dm_operate_park_car_month,dm_operate_park_car_line,dm_operate_park_space,dm_asset_overview,dm_asset_danger"
        self.table_name_cn = "基础物业_服务满意度_季,安全管护_上报隐患_月统计,安全管护_上报隐患_整改_月统计,安全管护_处理情况,能源管理_总览,能源管理_水能耗分析_月,能源管理_电能耗分析_月,能源管理_热能耗分析_月,能源管理_水能耗分布,能源管理_电能耗分布,智能运维_总览,智能运维_告警分类统计,智能运维_处理方式统计,智能运维_设备维保_月统计,综合态势_总览,综合态势_专项服务_月统计,综合态势_智慧通行,全国_概览,全国_军品物业_客户满意度_年,全国_军品物业_客户满意度_排名,全国_产业运营,分公司_概览,分公司_军品物业_客户满意度_年,分公司_军品物业_客户满意度_排名,分公司_产业运营,军品物业_概览,军品物业_客户满意度_年,军品物业_客户满意度_排名,军品物业_软文阅读量排行,军品物业_能源管控,军品物业_承接查验_类别分布,军品物业_承接查验_指标数,军品物业_承接查验_排名,军品物业_项目_概览,军品物业_项目_客户满意度,军品物业_项目_能源管控,产业运营_概览,产业运营_资产招租,产业运营_服务,产业运营_服务_企业服务_月,产业运营_服务_生活服务_月,产业运营_服务_车场运营,产业运营_服务_车场运营_当月营收,产业运营_服务_车场运营_单月停车,产业运营_服务_车场运营_盈亏数量,产业运营_服务_车场运营_空间运营,资产安全_概览,资产安全_隐患数量"
        self.grant_type = "SELECT,INSERT,UPDATE,DELETE"
        self.grant_schema = "USAGE"
        self.grant_user = "rtwg"

    def create_sql(self):
        table_name_array = self.table_name.split(",")
        table_name_cn_array = self.table_name_cn.split(",")
        grant_type_array = self.grant_type.split(",")

        with open('./tools/grant-sql/sql.txt','w',encoding="utf-8") as f:
            for item in table_name_array:
                # 截取dm_property名字
                schema_name = item[:item.index("_",3)]
                # 生成注释表明是哪个表
                print("-- " + table_name_cn_array[table_name_array.index(item)])
                f.writelines("-- " + table_name_cn_array[table_name_array.index(item)])
                f.writelines(" \n")
                # 生成授权查看schema的sql
                print("GRANT "+self.grant_schema+"  ON SCHEMA "+ schema_name +" TO "+self.grant_user+";")
                f.writelines("GRANT " + self.grant_schema + "  ON SCHEMA " + schema_name + " TO " + self.grant_user + ";")
                f.writelines(" \n")

                for j in grant_type_array:
                    print("GRANT "+j+" ON TABLE "+schema_name+"."+item+" TO "+self.grant_user+";")
                    # 生成授权查看表的sql
                    f.writelines("GRANT " + j + " ON TABLE " + schema_name + "." + item + " TO " + self.grant_user + ";")
                    f.writelines(" \n")
                print("\n")
                f.writelines(" \n")
            # 关闭输出
            f.close()

test = Test()
test.create_sql()