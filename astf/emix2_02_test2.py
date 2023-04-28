# This profile is using multiple pcaps in order to reach 1M active flows. We are using s_delay tunable in order to enlarge 
# each flow and increment total active flows. In order to avoid keepalive errors we're setting keepalive to 1.5 times the s_delay. 
# example start -f astf/emix2.py -m 30 -l 1000 -t traffic_per=0.9,s_delay=10000000
# will generate 30gbps with 90% of the traffic with no delay and 10% with delay of 10 sec betwean the packets 
#

from trex.astf.api import *
import random


MIN_CPS = 0.5
TREX_PATH = '/auto/proj-pcube-b/apps/PL-b/tools/bp_sim2/v2.81-gil'

class Prof1():
    def __init__(self):
        self.p = 1024  # starting port
        self.ka = None
        self.all_cap_info = []

    def sep_cap(self, file, cps, ip_gen=None, my_per=None):
        #my_per = my_per if my_per else self.traffic_per
        print(my_per)
        if my_per == None:
            
        else:

            
        assert 0 <= my_per <= 1.0, 'my_per should be in range: [0, 1]'
#        if my_per != None:
#             my_per
        my_per =1
        if 


        if my_per == 1:
            self.all_cap_info.append(ASTFCapInfo(file=file, cps=cps, ip_gen=ip_gen, port=self.p))
            self.p += 1
        elif my_per is None or my_per == 0:
            self.all_cap_info.append(ASTFCapInfo(file=file, cps=cps, ip_gen=ip_gen, port=self.p, s_delay=self.s_delay))
            self.p += 1
        else:
            normal_cps = cps * my_per
            delay_cps  = max(cps * (1 - my_per), MIN_CPS)

            normal_cap = ASTFCapInfo(file=file, cps=normal_cps, ip_gen=ip_gen, port=self.p)
            delay_cap  = ASTFCapInfo(file=file, cps=delay_cps, ip_gen=ip_gen, port=self.p + 1, s_delay=self.s_delay)
            self.all_cap_info.extend([normal_cap, delay_cap])
            self.p += 2

    def create_profile(self):
        # ip generator
        ip_gen_c = ASTFIPGenDist(ip_range=["16.0.0.1", "16.0.1.255"], distribution="seq")
        ip_gen_s = ASTFIPGenDist(ip_range=["48.0.0.1", "48.0.255.255"], distribution="seq")
        ip_gen = ASTFIPGen(glob=ASTFIPGenGlobal(ip_offset="1.0.0.0"),
                           dist_client=ip_gen_c,
                           dist_server=ip_gen_s)

        ip_gen_s_delay_10_http_get_0 = ASTFIPGenDist(ip_range=["48.1.0.1", "48.1.2.44"], distribution="seq")
        ip_gen_delay_10_http_get_0 = ASTFIPGen(glob=ASTFIPGenGlobal(ip_offset="1.0.0.0"),
                           dist_client=ip_gen_c,
                           dist_server=ip_gen_s_delay_10_http_get_0)

        ip_gen_s_delay_10_http_post_0 = ASTFIPGenDist(ip_range=["48.2.0.1", "48.2.2.44"], distribution="seq")
        ip_gen_delay_10_http_post_0 = ASTFIPGen(glob=ASTFIPGenGlobal(ip_offset="1.0.0.0"),
                           dist_client=ip_gen_c,
                           dist_server=ip_gen_s_delay_10_http_post_0)

        ip_gen_s_delay_10_https_0 = ASTFIPGenDist(ip_range=["48.3.0.1", "48.3.0.180"], distribution="seq")
        ip_gen_delay_10_https_0 = ASTFIPGen(glob=ASTFIPGenGlobal(ip_offset="1.0.0.0"),
                           dist_client=ip_gen_c,
                           dist_server=ip_gen_s_delay_10_https_0)

        ip_gen_s_delay_10_http_browsing_0 = ASTFIPGenDist(ip_range=["48.4.0.1", "48.4.3.209"], distribution="seq")
        ip_gen_delay_10_http_browsing_0 = ASTFIPGen(glob=ASTFIPGenGlobal(ip_offset="1.0.0.0"),
                           dist_client=ip_gen_c,
                           dist_server=ip_gen_s_delay_10_http_browsing_0)

        ip_gen_s_delay_10_exchange_0 = ASTFIPGenDist(ip_range=["48.5.0.1", "48.5.1.93"], distribution="seq")
        ip_gen_delay_10_exchange_0 = ASTFIPGen(glob=ASTFIPGenGlobal(ip_offset="1.0.0.0"),
                           dist_client=ip_gen_c,
                           dist_server=ip_gen_s_delay_10_exchange_0)

        ip_gen_s_delay_10_mail_pop_0 = ASTFIPGenDist(ip_range=["48.6.0.1", "48.6.0.40"], distribution="seq")
        ip_gen_delay_10_mail_pop_0 = ASTFIPGen(glob=ASTFIPGenGlobal(ip_offset="1.0.0.0"),
                           dist_client=ip_gen_c,
                           dist_server=ip_gen_s_delay_10_mail_pop_0)

        ip_gen_s_delay_10_mail_pop_1 = ASTFIPGenDist(ip_range=["48.7.0.1", "48.7.0.40"], distribution="seq")
        ip_gen_delay_10_mail_pop_1 = ASTFIPGen(glob=ASTFIPGenGlobal(ip_offset="1.0.0.0"),
                           dist_client=ip_gen_c,
                           dist_server=ip_gen_s_delay_10_mail_pop_1)

        ip_gen_s_delay_10_mail_pop_2 = ASTFIPGenDist(ip_range=["48.8.0.1", "48.8.0.40"], distribution="seq")
        ip_gen_delay_10_mail_pop_2 = ASTFIPGen(glob=ASTFIPGenGlobal(ip_offset="1.0.0.0"),
                           dist_client=ip_gen_c,
                           dist_server=ip_gen_s_delay_10_mail_pop_2)

        ip_gen_s_delay_10_oracle_0 = ASTFIPGenDist(ip_range=["48.9.0.1", "48.9.0.109"], distribution="seq")
        ip_gen_delay_10_oracle_0 = ASTFIPGen(glob=ASTFIPGenGlobal(ip_offset="1.0.0.0"),
                           dist_client=ip_gen_c,
                           dist_server=ip_gen_s_delay_10_oracle_0)

        ip_gen_c_rtsp_rtp = ASTFIPGenDist(ip_range=["16.10.0.1", "16.10.1.255"], distribution="seq")
        ip_gen_s_rtsp_rtp = ASTFIPGenDist(ip_range=["48.10.0.1", "48.10.1.255"], distribution="seq")
        ip_gen_rtsp_rtp = ASTFIPGen(glob=ASTFIPGenGlobal(ip_offset="1.0.0.0"),
                           dist_client=ip_gen_c_rtsp_rtp,
                           dist_server=ip_gen_s_rtsp_rtp)

        ip_gen_s_delay_10_smtp_0 = ASTFIPGenDist(ip_range=["48.12.0.1", "48.12.0.40"], distribution="seq")
        ip_gen_delay_10_smtp_0 = ASTFIPGen(glob=ASTFIPGenGlobal(ip_offset="1.0.0.0"),
                           dist_client=ip_gen_c,
                           dist_server=ip_gen_s_delay_10_smtp_0)

        ip_gen_s_delay_10_smtp_1 = ASTFIPGenDist(ip_range=["48.13.0.1", "48.13.0.40"], distribution="seq")
        ip_gen_delay_10_smtp_1 = ASTFIPGen(glob=ASTFIPGenGlobal(ip_offset="1.0.0.0"),
                           dist_client=ip_gen_c,
                           dist_server=ip_gen_s_delay_10_smtp_1)

        ip_gen_s_delay_10_smtp_2 = ASTFIPGenDist(ip_range=["48.14.0.1", "48.14.0.40"], distribution="seq")
        ip_gen_delay_10_smtp_2 = ASTFIPGen(glob=ASTFIPGenGlobal(ip_offset="1.0.0.0"),
                           dist_client=ip_gen_c,
                           dist_server=ip_gen_s_delay_10_smtp_2)

        ip_gen_c_sip_rtp = ASTFIPGenDist(ip_range=["16.16.0.1", "16.16.1.255"], distribution="seq")
        ip_gen_s_sip_rtp = ASTFIPGenDist(ip_range=["48.16.0.1", "48.16.1.255"], distribution="seq")
        ip_gen_sip_rtp = ASTFIPGen(glob=ASTFIPGenGlobal(ip_offset="1.0.0.0"),
                           dist_client=ip_gen_c_sip_rtp,
                           dist_server=ip_gen_s_sip_rtp)

        ip_gen_s_delay_10_citrix_0 = ASTFIPGenDist(ip_range=["48.17.0.1", "48.17.0.60"], distribution="seq")
        ip_gen_delay_10_citrix_0 = ASTFIPGen(glob=ASTFIPGenGlobal(ip_offset="1.0.0.0"),
                           dist_client=ip_gen_c,
                           dist_server=ip_gen_s_delay_10_citrix_0)

        ip_gen_s_delay_10_dns_0 = ASTFIPGenDist(ip_range=["48.18.0.1", "48.18.10.158"], distribution="seq")
        ip_gen_delay_10_dns_0 = ASTFIPGen(glob=ASTFIPGenGlobal(ip_offset="1.0.0.0"),
                           dist_client=ip_gen_c,
                           dist_server=ip_gen_s_delay_10_dns_0)

        c_glob_info = ASTFGlobalInfo()
        s_glob_info = ASTFGlobalInfo()
        if self.ka is not None:
            c_glob_info.tcp.keepinit = self.ka
            c_glob_info.tcp.keepidle = self.ka
            c_glob_info.tcp.keepintvl = self.ka

            s_glob_info.tcp.keepinit = self.ka
            s_glob_info.tcp.keepidle = self.ka
            s_glob_info.tcp.keepintvl = self.ka

        #self.sep_cap(file=TREX_PATH+"/avl/http_manual_01.pcap_c.pcap", cps=123.02, ip_gen=ip_gen_delay_10_http_get_0),
        #self.sep_cap(file=TREX_PATH+"/avl/delay_10_http_post_0.pcap", cps=123.02, ip_gen=ip_gen_delay_10_http_post_0),


        #self.sep_cap(file=TREX_PATH+"/avl/delay_10_https_0.pcap", cps=544.8, ip_gen=ip_gen_delay_10_https_0),
        #elf.sep_cap(file=TREX_PATH+"/avl/http_manual_02.pcap_c.pcap", cps=70.3, ip_gen=ip_gen_delay_10_http_browsing_0),


        #self.sep_cap(file=TREX_PATH+"/avl/delay_10_exchange_0.pcap", cps=667.81, ip_gen=ip_gen_delay_10_exchange_0),

        #self.sep_cap(file=TREX_PATH+"/avl/delay_10_mail_pop_1.pcap", cps=27.42, ip_gen=ip_gen_delay_10_mail_pop_1),


        #self.sep_cap(file=TREX_PATH+"/avl/delay_10_rtp_160k_0.pcap", cps=2.46, ip_gen=ip_gen_rtsp_rtp, my_per=0),
        #self.sep_cap(file=TREX_PATH+"/avl/delay_10_rtp_160k_1.pcap", cps=2.46, ip_gen=ip_gen_rtsp_rtp, my_per=0),
        #self.sep_cap(file=TREX_PATH+"/avl/delay_10_rtp_250k_0_0.pcap", cps=1.76, ip_gen=ip_gen_rtsp_rtp, my_per=0),
        #self.sep_cap(file=TREX_PATH+"/avl/delay_10_rtp_250k_1_0.pcap", cps=1.76, ip_gen=ip_gen_rtsp_rtp, my_per=0),

        #self.sep_cap(file=TREX_PATH+"/avl/delay_10_smtp_2.pcap", cps=28.12, ip_gen=ip_gen_delay_10_smtp_2),

        #self.sep_cap(file=TREX_PATH+"/avl/delay_10_video_call_0.pcap", cps=5.27, ip_gen=ip_gen_rtsp_rtp, my_per=0),

        #self.sep_cap(file=TREX_PATH+"/avl/delay_10_video_call_rtp_0.pcap", cps=26.36, ip_gen=ip_gen_sip_rtp, my_per=0),

        self.sep_cap(file=TREX_PATH+"/avl/delay_10_citrix_0.pcap", cps=70.3, ip_gen=ip_gen_delay_10_citrix_0, my_per=0),
        self.sep_cap(file=TREX_PATH+"/avl/delay_10_dns_0.pcap", cps=274.86, ip_gen=ip_gen_delay_10_dns_0),

        #self.sep_cap(file=TREX_PATH+"/avl/delay_10_sip_0.pcap", cps=26.36, ip_gen=ip_gen_sip_rtp, my_per=0),
        #self.sep_cap(file=TREX_PATH+"/avl/delay_10_rtsp_0.pcap", cps=4.22, ip_gen=ip_gen_rtsp_rtp, my_per=0),

        profile = ASTFProfile(default_ip_gen=ip_gen,
            default_c_glob_info=c_glob_info,
            default_s_glob_info=s_glob_info,
            cap_list = self.all_cap_info
        )

        return profile

    def get_profile(self, **kwargs):
        ka          = kwargs.get('tcp_ka', None)       # tcp keepalive 
        s_delay     = kwargs.get('s_delay', None)      # delay for server, in usec
        traffic_per = kwargs.get('traffic_per', None)  # how much of the traffic will have no delay, should be in range: [0, 1]
        port        = kwargs.get('port', None)         # starting port, inc by 1 for each capinfo

        if s_delay is not None:
            assert s_delay > 0, 's_delay must be positive'
            s_delay = int(s_delay)
           #d = random.randint(s_delay // 10, s_delay)
            d = s_delay
            s_delay = ASTFCmdDelay(d)
            new_ka = int((d / 1000) * 1.5)
            self.ka = min(new_ka, 65533)    # 65533 is max keepalive val 

        if ka is not None:
            self.ka = int(ka)

        if traffic_per is not None:
            assert 0.0 <= traffic_per <= 1.0, 'traffic_per must be in range [0,1]'
            traffic_per = float(traffic_per)

        if port is not None:
            self.p = port

        self.s_delay     = s_delay
        self.traffic_per = traffic_per
        return self.create_profile()


def register():
    return Prof1()

