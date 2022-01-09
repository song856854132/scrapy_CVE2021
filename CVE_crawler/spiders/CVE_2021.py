import scrapy
# CVE2021(12mon) >> month(30pages) >> items(href)

# while (next page)
    # crawl info from main page
    # crawl href link to get product type, vendor, product name, and cvss score
    # goto next page
class CVEspider(scrapy.Spider):
    name = "crawl_cvedetail"
    basic_url = 'https://www.cvedetails.com/'
    start_urls = [
        # 'https://www.cvedetails.com/vulnerability-list.php?vendor_id=0&product_id=0&version_id=0&page=1&hasexp=0&opdos=0&opec=0&opov=0&opcsrf=0&opgpriv=0&opsqli=0&opxss=0&opdirt=0&opmemc=0&ophttprs=0&opbyp=0&opfileinc=0&opginf=0&cvssscoremin=0&cvssscoremax=0&year=2021&month=1&cweid=0&order=1&trc=1524&sha=2ef19897dfbffbbd5a04a5f70124230a5b04f151'
        basic_url + "vulnerability-list.php?vendor_id=0&product_id=0&version_id=0&page=1&hasexp=0&opdos=0&opec=0&opov=0&opcsrf=0&opgpriv=0&opsqli=0&opxss=0&opdirt=0&opmemc=0&ophttprs=0&opbyp=0&opfileinc=0&opginf=0&cvssscoremin=0&cvssscoremax=0&year=0&month=0&cweid=0&order=1&trc=167409&sha=3cf9994d68386594f1283fc226cf51dad5fe72b8",
        basic_url + "vulnerability-list.php?vendor_id=0&product_id=0&version_id=0&page=2&hasexp=0&opdos=0&opec=0&opov=0&opcsrf=0&opgpriv=0&opsqli=0&opxss=0&opdirt=0&opmemc=0&ophttprs=0&opbyp=0&opfileinc=0&opginf=0&cvssscoremin=0&cvssscoremax=0&year=0&month=0&cweid=0&order=1&trc=167409&sha=3cf9994d68386594f1283fc226cf51dad5fe72b8",
        basic_url + "vulnerability-list.php?vendor_id=0&product_id=0&version_id=0&page=3&hasexp=0&opdos=0&opec=0&opov=0&opcsrf=0&opgpriv=0&opsqli=0&opxss=0&opdirt=0&opmemc=0&ophttprs=0&opbyp=0&opfileinc=0&opginf=0&cvssscoremin=0&cvssscoremax=0&year=0&month=0&cweid=0&order=1&trc=167409&sha=3cf9994d68386594f1283fc226cf51dad5fe72b8",
        basic_url + "vulnerability-list.php?vendor_id=0&product_id=0&version_id=0&page=4&hasexp=0&opdos=0&opec=0&opov=0&opcsrf=0&opgpriv=0&opsqli=0&opxss=0&opdirt=0&opmemc=0&ophttprs=0&opbyp=0&opfileinc=0&opginf=0&cvssscoremin=0&cvssscoremax=0&year=0&month=0&cweid=0&order=1&trc=167409&sha=3cf9994d68386594f1283fc226cf51dad5fe72b8",
        basic_url + "vulnerability-list.php?vendor_id=0&product_id=0&version_id=0&page=5&hasexp=0&opdos=0&opec=0&opov=0&opcsrf=0&opgpriv=0&opsqli=0&opxss=0&opdirt=0&opmemc=0&ophttprs=0&opbyp=0&opfileinc=0&opginf=0&cvssscoremin=0&cvssscoremax=0&year=0&month=0&cweid=0&order=1&trc=167409&sha=3cf9994d68386594f1283fc226cf51dad5fe72b8"

    ]

    def parse(self, response, basic_url):
        for href in response.xpath(".//td[@nowrap]/a/@href"):
            print(href)
            yield scrapy.Request(basic_url+href, callback = self.parse_dir_contents)
    
    def parse_dir_contents(self, response):
        yield{
            # 'url': response.xpath(".//td[@nowrap]/a/@href"), # //div[@id='searchresults']/table[@class='searchresults sortable']/tr[@class='srrowns']/td[@nowrap]/a/@href
            'severity': response.css("div.cvssbox::text"),
            'cve': response.css("h1>a::text"),
            'product_type': ,
            'vendor': self.formatting(vendors),
            'product':
        }


















    # add a try and exception for 
    # def parse(self, response):


    #     for prod in : # crawl into the url of CVE, and check the vuln product
    #         try:
    #             yield{
    #             # 'title':self.formatting(CVE),
    #             'url': response.xpath(".//td[@nowrap]/a/@href"), # //div[@id='searchresults']/table[@class='searchresults sortable']/tr[@class='srrowns']/td[@nowrap]/a/@href
    #             'severity': response.xpath(".//td/div[@class='cvssbox']/text()"),
    #             'cve': response.xpath(".//td[@nowrap]/a/text()"),
    #             'product_type': ,
    #             'vendor': self.formatting(vendors),
    #             'product':
    #             # 'publishedDate': self.formatting(publish_date),
    #             # 'modifiedDate': self.formatting(last_update_date),
    #             # 'affectedProducts': self.formatting(affected_products),
    #             # 'description':self.formatting(description),
    #         }
    #         except:
    #             yield{
    #                 # 'title':self.formatting(CVE),
    #                 'url': response.xpath(".//td[@nowrap]/a/@href"), # //div[@id='searchresults']/table[@class='searchresults sortable']/tr[@class='srrowns']/td[@nowrap]/a/@href
    #                 'severity': response.xpath(".//td/div[@class='cvssbox']/text()"),
    #                 'cve': response.xpath(".//td[@nowrap]/a/text()"),
    #                 'product_type': 'none',
    #                 'vendor': 'none',
    #                 'product': 'none'
    #                 # 'publishedDate': self.formatting(publish_date),
    #                 # 'modifiedDate': self.formatting(last_update_date),
    #                 # 'affectedProducts': self.formatting(affected_products),
    #                 # 'description':self.formatting(description),
    #             }
    
    # def pageBypage(self, response):
    #     for page in start_urls:
    #         yield 

    # def formatting(self,content):
    #     if isinstance(content,list):
    #         content = ''.join(content).strip()
    #     else:
    #         content = content.strip()
    #     if content[-1] is ',':
    #         content = content[:-1]
    #     return content