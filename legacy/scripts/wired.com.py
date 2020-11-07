from legacy.crawler import crawler
import os

url = "https://www.wired.com"
output_dir = os.path.join('../..', 'data', 'wired.com')
headers = {
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding':'*',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Cookie': 'pay_ent_smp=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsInZlciI6MX0.eyJ1cmxzIjpbIi8yMDAxLzAzL2hvbmV5cG90cy1iYWl0LWZvci10aGUtY3JhY2tlciJdLCJjbnQiOjEsIm1heCI6NCwiZXhwIjoyMDE4MTB9.SvGXeHRGxLna6rX9Kr9qTXrSU-pSbIkrDE_hQwQ60O4; CN_xid=d75239c8-659c-476c-9f5d-ea0547275e55; _sdsat_landing_page=https://www.wired.com/2001/03/honeypots-bait-for-the-cracker/|1540044766455; _sdsat_session_count=1; _sdsat_traffic_source=https://www.google.com.hk/; visitedCount_jwt=1; AMCVS_F7093025512D2B690A490D44%40AdobeOrg=1; CN_sp=fa58760d-4e72-4ce3-b443-2c9b42243770; CN_su=d19800c0-59da-4191-a88c-5c4148ebb692; CN_segments=; _ga=GA1.2.802886981.1540044768; fpcid=2456436582056134046_FP; v30=google.com.hk; v39=google.com.hk; s_cc=true; __gads=ID=f8c89cd159acd50f:T=1540044768:S=ALNI_MainR0wk-mflQoNeN_UO7dory-7gQ; aamconde=conde%3Dsv%3BCN%3D764985; aam_optimizely=aam%3D226821; aam_uuid=26426712967223226083480932539320192677; _sdsat_lt_pages_viewed=2; _sdsat_pages_viewed=2; _sdsat_AAM_UUID=26426712967223226083480932539320192677; CN_visits_m=1541001600572%26vn%3D2; CN_in_visit_m=true; sID=2955f7c3-91dd-4bc7-abc7-999968ecee3c; pID=1d3e3648-9926-466b-beec-6a2e98c8702c; AMCV_F7093025512D2B690A490D44%40AdobeOrg=1099438348%7CMCIDTS%7C17834%7CMCMID%7C26574736731012813853459705698242364028%7CMCAAMLH-1541404553%7C3%7CMCAAMB-1541404553%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1540806953s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C2.1.0; s_vnum_m=1541001600667%26vn%3D2; sinvisit_m=true; s_depth=1; timeSpent=1540799753187; s_ppn=https%3A%2F%2Fwww.wired.com%2Fcategory%2Fsecurity%2Fthreatlevel%2F; s_pct=Index; s_nr=1540799753188-Repeat; sailthru_pageviews=1; bounceClientVisit2825v=N4IgNgDiBcIBYBcEQM4FIDMBBNAmAYnvgO6kB0xAlgE4CmAJmQMYD2AtkUwIYK0DmLagE8iCOHR5haAN1pgiIADQhqMECAC+QA; _polar_tu=*_%22mgtn%22_@2Q_u_@_97f78f97-5c77-4716-b78f-a0dccc974ab0_Q_n_@3Q_s_@2Q_sc_@*_v_@1Q_a_@1+Q_ss_@_%22phcop7_Q_sl_@_%22phcop7_Q_sd_@*+Q_v_@nullQ_vc_@*_e_@0+Q_vs_@_%22phcop7_Q_vl_@_%22phcop7_Q_vd_@*+Q_vu_@_555fdf068442e929ddada46236b2ea5b_Q_vf_@_%22jnu0e179_+; _parsely_session={%22sid%22:2%2C%22surl%22:%22https://www.wired.com/category/threatlevel/%22%2C%22sref%22:%22%22%2C%22sts%22:1540799755083%2C%22slts%22:1540044768270}; _parsely_visitor={%22id%22:%22c609b887-dad6-414c-906e-f6a107dbb880%22%2C%22session_count%22:2%2C%22last_session_ts%22:1540799755083}; sailthru_content=e43720c11f5345e88d86bc1d5be31f74e2553d06f8d9ea3b9cb7420abe100f46; sailthru_visitor=1cb98baf-6809-4646-a0f8-aa82685e000a; AMP_TOKEN=%24NOT_FOUND; _gid=GA1.2.368334264.1540799760',
        'Connection':'keep-alive',
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/70.0.3538.67 Chrome/70.0.3538.67 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest'
        }

if __name__ == "__main__":
    wpc = crawler.WordPressCrawler(url, headers)
    wpc.get_tags(os.path.join('{}'.format(output_dir), 'tags.json'))
    wpc.get_categories(os.path.join('{}'.format(output_dir), 'cats.json'))
    wpc.get_posts(os.path.join('{}'.format(output_dir), 'posts.json'))