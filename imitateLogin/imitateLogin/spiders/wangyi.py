import scrapy


class WangyiSpider(scrapy.Spider):
    name = 'wangyi'
    allowed_domains = ['mail.163.com']
    start_urls = ['https://mail.163.com/js6/main.jsp?sid=aAfyewTFGcZBzjGYrZFFXRmialFRhkzi&df=mail163_letter']
    cookies = "9755xjdesxxd_=32; MAIL_SDID=895610059806744576; locale=; face=js6; _ntes_nnid=04560cd29fb005de4a19245b6e50a257,1665108461335; _ntes_nuid=04560cd29fb005de4a19245b6e50a257; nts_mail_user=wy19558986127@163.com:-1:1; __root_domain_v=.163.com; _qddaz=QD.925665495174534; wyy_uid=601e819c-db44-4f38-82e2-ac8842fe0058; channel='h=yd&t=yd&i18nEnable=true&locale=zh_CN&referrer=https%3A%2F%2Fdun.163.com%2Fdashboard&fromyd=baiduP2_YZM_CP6302'; hb_MA-91DF-2127272A00D5_source=dun.163.com; locale=zh_CN; _gcl_au=1.1.699266739.1665495318; hb_MA-93D5-9AD06EA4329A_source=www.baidu.com; __bid_n=183c989a6abf07c7744207; gdxidpyhxdE=7UwDxByXewGUpLLWDh%2FGie8bU9S8N2NRZIA5ST%5CbXtQOAeoYRJUS%2BLgv8eJX4Ar%2F6b9WnbaU8hwuiTMdC%5CCC%5CWdj%2FSu%5CvU6SEi6hDMbYZmaGaG8iAwQ1dX%5CrxuBaSzzSmXAUHr%2BlpI6ssTaw3kkI2YUqekZbkMSE%2B3fzN91%2BQnxMaxEJ%3A1665534500048; _pk_ref.16.b4c4=%5B%22%22%2C%22%22%2C1665884988%2C%22https%3A%2F%2Fmusic.163.com%2F%22%5D; _pk_id.16.b4c4=eb578addcc2287e2.1665654707.3.1665884988.1665756248.; starttime=; NTES_P_UTID=l1uA4G8vGyxu28GMn0rs9D1CsUvkxd59|1666362727; NTES_SESS=SICkZvyYoyAmV0rw3oco42czMy6qmCuFDf4fTlBrzvPQd3GbdnHABwBcSBKMmFfWV1PVrBjHlo85i5LCsl7Ow42FA9B1E9RDZ7zlRWl_AEZMJ8hQB_n9M339jzBf0AQRM_GxDNGwu_D0kM.Ntyz6iLfx_Xn2kZsUcaRWSxJDVJEPNE_e9P_TyZcG3ecgAvijVTtrlb7ig7NQw; S_INFO=1666362727|0|3&80##|wy19558986127; P_INFO=wy19558986127@163.com|1666362727|0|mail163|00&99|shd&1665126468&mail163#shd&370600#10#0#0|&0||wy19558986127@163.com; df=mail163_letter; mail_idc=""; Coremail=490e66a3f5706%aAfyewTFGcZBzjGYrZFFXRmialFRhkzi%g3a24.mail.163.com; MAIL_ENTRY_INFO=1|0|mail163|mail163_letter|111.15.84.241|63b4e444414396887ccd883218dbb6be_v1|; MAIL_ENTRY_CS=992fc5eecd9c6bdd1aadd2754eac1f3d; cm_last_info=dT13eTE5NTU4OTg2MTI3JTQwMTYzLmNvbSZkPWh0dHBzJTNBJTJGJTJGbWFpbC4xNjMuY29tJTJGanM2JTJGbWFpbi5qc3AlM0ZzaWQlM0RhQWZ5ZXdURkdjWkJ6akdZclpGRlhSbWlhbEZSaGt6aSZzPWFBZnlld1RGR2NaQnpqR1lyWkZGWFJtaWFsRlJoa3ppJmg9aHR0cHMlM0ElMkYlMkZtYWlsLjE2My5jb20lMkZqczYlMkZtYWluLmpzcCUzRnNpZCUzRGFBZnlld1RGR2NaQnpqR1lyWkZGWFJtaWFsRlJoa3ppJnc9aHR0cHMlM0ElMkYlMkZtYWlsLjE2My5jb20mbD0tMSZ0PS0xJmFzPXRydWU=; MAIL_SESS=SICkZvyYoyAmV0rw3oco42czMy6qmCuFDf4fTlBrzvPQd3GbdnHABwBcSBKMmFfWV1PVrBjHlo85i5LCsl7Ow42FA9B1E9RDZ7zlRWl_AEZMJ8hQB_n9M339jzBf0AQRM_GxDNGwu_D0kM.Ntyz6iLfx_Xn2kZsUcaRWSxJDVJEPNE_e9P_TyZcG3ecgAvijVTtrlb7ig7NQw; MAIL_SINFO=1666362727|0|3&80##|wy19558986127; MAIL_PINFO=wy19558986127@163.com|1666362727|0|mail163|00&99|shd&1665126468&mail163#shd&370600#10#0#0|&0||wy19558986127@163.com; secu_info=1; mail_entry_sess=2513f31c487761c7452ee5671046987c157f6548242bef87f81b62ddab062e8c9abd91624ebacca11833c6361638fd4ccbe5e9f4919ac56c57654ac3b8f68bdf0c9c3609df263b1f901e6eb6f9678e06a9a3818e7d6afef853a923d1267eed1d0d973b90dc24abdf34e80d2f674d398659272ec8bef883718a83f93552c9adc95fce3fa65029621d05247061a30b1f3963b644344f9f8a1fd26ae9e3fe81e96562c52e5dd7ee946759196d9aafd81c50913355f434707bad76a4a1f1fd128f81; JSESSIONID=647DD0F3B08ACFD73E8B51D48A5181B7; Coremail.sid=aAfyewTFGcZBzjGYrZFFXRmialFRhkzi; mail_style=js6; mail_uid=wy19558986127@163.com; mail_host=mail.163.com; stats_session_id=83606dde-a134-46b3-8315-e821aa8763b5; gateAbtestInfo=%7B%22abZone%22%3A%22B%22%2C%22abVersion%22%3A%221.0.1%22%2C%22t%22%3A1666362729579%2C%22sign%22%3A%2269ea1a00d201617db75c07c3fa7eded7%22%7D"
    cookies_dict = {item.split('=')[0]:item.split('=')[0] for item in cookies.split(";")}


    def start_requests(self):
        yield scrapy.Request(self.start_urls[0],cookies=self.cookies_dict,callback=self.parse)


    def parse(self, response):
        print('*' * 100)
        print(response)
        print('*' * 100)
        with open('1111.html','w',encoding='utf-8') as f:
            f.write(response.body.decode())
