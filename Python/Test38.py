# Generate email

import random

ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'

DOMAINS = (
    "gmail.com", "hotmail.com", "yahoo.com", "i.ua"
)

SOURCE = """
1	James	4,663,035	Mary	3,124,584
2	Robert	4,407,377	Patricia	1,555,054
3	John	4,403,862	Jennifer	1,469,031
4	Michael	4,340,931	Linda	1,448,283
5	David	3,564,313	Elizabeth	1,411,916
6	William	3,524,670	Barbara	1,391,959
7	Richard	2,439,835	Susan	1,103,018
8	Joseph	2,317,860	Jessica	1,047,000
9	Thomas	2,143,281	Sarah	989,810
10	Charles	2,060,835	Karen	986,072
11	Christopher	2,044,437	Lisa	965,015
12	Daniel	1,900,488	Nancy	963,833
13	Matthew	1,614,109	Betty	906,997
14	Anthony	1,407,623	Margaret	892,334
15	Mark	1,348,322	Sandra	873,655
16	Donald	1,323,467	Ashley	851,020
17	Steven	1,283,686	Kimberly	841,144
18	Paul	1,263,912	Emily	835,442
19	Andrew	1,255,723	Donna	821,223
20	Joshua	1,226,213	Michelle	813,153
21	Kenneth	1,212,646	Carol	804,807
22	Kevin	1,176,784	Amanda	773,501
23	Brian	1,169,267	Dorothy	772,958
24	George	1,110,560	Melissa	754,784
25	Timothy	1,072,620	Deborah	740,223
26	Ronald	1,072,270	Stephanie	738,905
27	Edward	1,060,576	Rebecca	729,447
28	Jason	1,041,127	Sharon	720,831
29	Jeffrey	976,651	Laura	714,847
30	Ryan	947,756	Cynthia	705,778
31	Jacob	941,181	Kathleen	683,064
32	Gary	900,277	Amy	682,347
33	Nicholas	896,856	Angela	659,597
34	Eric	880,874	Shirley	657,764
35	Jonathan	853,162	Anna	607,022
36	Stephen	838,395	Brenda	606,299
37	Larry	802,063	Pamela	592,699
38	Justin	781,577	Emma	591,173
39	Scott	770,208	Nicole	590,414
40	Brandon	763,634	Helen	584,461
41	Benjamin	749,881	Samantha	581,626
42	Samuel	717,912	Katherine	568,258
43	Gregory	707,931	Christine	558,861
44	Alexander	683,727	Debra	548,281
45	Frank	675,530	Rachel	545,873
46	Patrick	665,520	Carolyn	539,223
47	Raymond	657,165	Janet	537,105
48	Jack	635,483	Catherine	534,876
49	Dennis	610,810	Maria	529,993
50	Jerry	601,368	Heather	524,171
51	Tyler	594,971	Diane	515,112
52	Aaron	588,205	Ruth	514,443
53	Jose	565,276	Julie	506,856
54	Adam	557,653	Olivia	498,779
55	Nathan	554,162	Joyce	497,784
56	Henry	552,869	Virginia	496,631
57	Douglas	546,783	Victoria	489,302
58	Zachary	543,288	Kelly	471,945
59	Peter	537,153	Lauren	471,879
"""

NAMES = []


for item in SOURCE.split():
    if item.isalpha():
        NAMES.append(item.lower())


def generate_email(name=None):
    domain = random.choice(DOMAINS)
    nick = name if name else random.choice(NAMES)

    temp = ""
    for _ in range(15):
        char = random.choice(ascii_lowercase)
        temp += char

    return f'{nick}@{domain}'


if __name__ == "__main__":
    result_email = (generate_email())
    print(result_email)
