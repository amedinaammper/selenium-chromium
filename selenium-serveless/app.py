import json
import requests
from urllib.parse import unquote
from selenium_connect import SeleniumConnect
from s3_connect import S3Connect

def lambda_handler(event, context):
    
    #s3 = S3Connect()
    #r = requests.get("https://www.cenace.gob.mx/Docs/09_OPESEN/GenMantenimiento/2021/2021-06%20Pron%C3%B3stico%20Capacidad%20Generaci%C3%B3n%20Mantenimiento%202021-2023.xlsx")
    #s3.uploadObject(r.content,"cenace.xlsx")

    s = SeleniumConnect("https://www.cenace.gob.mx/Paginas/SIM/DisponibilidadGeneracion.aspx")
    driver = s.driverChrome()
    
    s3 = S3Connect()
    
    table = driver.find_element_by_xpath("//div[@id='panel1']/div[@class='contenidoTabsFijo']/table/tbody")
    
    for row in table.find_elements_by_xpath(".//tr"):
        for td in row.find_elements_by_xpath(".//td[2]"):
            urlFile = td.find_element_by_xpath(".//a").get_attribute('href')
            n = urlFile.split('/')
            file_name = unquote(n[len(n)-1]);
            route_file = '/tmp/' + file_name
            route_file_s3 = 'cenace/' + file_name
            r = requests.get(urlFile)
            s3.uploadObject(r.content,route_file_s3)
            #print("UPLOAD:" + file_name)
    

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            # "location": ip.text.replace("\n", "")
        }),
    }
