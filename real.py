from bs4 import BeautifulSoup
import requests,time


print('Put the skill that you dont have')
unfamiliar_skill= input('>')
print('filtering out {unfamiliar_skill}')


def finding_job():

    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

    #print(html_text)

    soup=BeautifulSoup(html_text,'lxml')
    job= soup.find_all('li',class_='clearfix job-bx wht-shd-bx')

    #print(jobs)
    for index,jobs in enumerate(job):

        
        published_date=jobs.find('span',class_='sim-posted')
        demp=published_date.find('span').text

        if 'few' in demp:


            company_name=jobs.find('h3',class_='joblist-comp-name')
            skills=jobs.find('span',class_='srp-skills')
            updated_skills=(skills.text.replace(' ',''))
            updated_company_name=(company_name.text.replace(' ',''))
            more=jobs.header.h2.a['href'].replace('//','')
            published_date=jobs.find('span',class_='sim-posted')
            demp=published_date.find('span').text

            #print(published_date)
            



        #This replace method is replaching ' ' white space with nospace('')

            if unfamiliar_skill not in updated_skills:
                with open(f'post/{index}.txt','w') as f:
                    


                    print(f'Company name: {updated_company_name.strip()} \n')
                    print(f'Required Skill: {updated_skills.strip()} \n')
                    print(f'Job Link:{more}\n')



                    f.write(f'Company name: {updated_company_name.strip()} \n')
                    f.write(f'Required Skill: {updated_skills.strip()} \n')
                    f.write(f'Job Link:{more} \n')

                print(f'File saved into {index}')


                    
            


if __name__=='__main__':
    while True:
        finding_job()
        waiting_time=10
        print(f'wating for {waiting_time} min......')
        time.sleep(waiting_time*60)
