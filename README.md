# scrapy crawler for CVE 

## How to use it

### Pre-Request
- Git
- Python & scrapy
### Install and Run 
```shell=
└─$ git clone
└─$ cd scrapy_CVE; scrapy crawl spider_XXXX
```
After running the command, you can sit back and chill. It will take certain amount of time depend on the scope you crawl and network bandwith you have.

## Result and Explain
This script aimed at spider all CVE in [CVE-list directories](https://www.cvedetails.com/vulnerability-list/). The script only collect 5 culums, which were CVE, CVSS score, Product Type, Vendor, and Product Name, which were shown below.  

```shell=
└─$ head 2020_Hardware.csv 
cve,severity,product_type,vendor,product
CVE-2021-0144,4.6,Hardware,Intel,Core I7-3820
CVE-2021-0144,4.6,Hardware,Intel,Core I7-3920xm
CVE-2021-0144,4.6,Hardware,Intel,Core I7-3930k
CVE-2021-0144,4.6,Hardware,Intel,Core I7-3940xm
CVE-2021-0144,4.6,Hardware,Intel,Core I7-3960x
CVE-2021-0144,4.6,Hardware,Intel,Core I7-3970x
CVE-2021-0144,4.6,Hardware,Intel,Core I7-4820k
CVE-2021-0144,4.6,Hardware,Intel,Core I7-4930k
CVE-2021-0158,4.6,Hardware,Intel,Celeron N2806
CVE-2021-0144,4.6,Hardware,Intel,Core I7-4930mx
CVE-2021-0158,4.6,Hardware,Intel,Celeron N2807
CVE-2021-0157,4.6,Hardware,Intel,Celeron N2806
CVE-2021-0144,4.6,Hardware,Intel,Core I7-4940mx
```
It's was a simple script wrote for my colleague.