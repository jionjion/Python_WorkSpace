# -*- coding: utf-8 -*-

import requests
# http://10.18.111.128/hls/modules/batch_download/prj_elec_download.svc?table_pk_value=,77491&table_name=,CS_PRJ_FINANCIAL_STATEMENTS&doc_code=PROJECT_ZIP


if __name__ == '__main__':
     res = requests.get("http://10.18.111.128/hls/modules/batch_download/prj_elec_download.svc?table_pk_value=,77491&table_name=,CS_PRJ_FINANCIAL_STATEMENTS&doc_code=PROJECT_ZIP")
     with open("file.zip", 'wb') as file_text:
          file_text.write(res.content)