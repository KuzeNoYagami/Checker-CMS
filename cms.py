import multiprocessing
import requests
import re

def cms_checker(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            content = response.text
            if re.search('wp-content|wordpress', content, re.I):
                with open('wordpress.txt', 'a+') as f:
                    f.write(url + '\n')

            elif re.search('laravel_session|laravel', content, re.I):
                with open('laravel.txt', 'a+') as f:
                    f.write(url + '\n')

            elif re.search('joomla', content, re.I):
                with open('joomla.txt', 'a+') as f:
                    f.write(url + '\n')

            elif re.search('drupal', content, re.I):
                with open('drupal.txt', 'a+') as f:
                    f.write(url + '\n')

            else:  # other cms 
                with open('others.txt', 'a+') as f:  # save to others file 
                    f.write(url + '\n')

    except Exception as e:  # handle exception 
        print(e)

    finally:  # print the url which is checked 
        print("Checked : " + url)

        
if __name__ == "__main__":  # main function 

    urls = []  # list of urls to check 

    with open("list.txt", "r") as f:  # read the list of urls from file list.txt 

        for line in f:  # iterate over each line in the file 

            line = line.strip()  # remove extra spaces if any  

            if line != "":   # check if line is not empty  

                urls.append(line)   # append the url to the list  

    pool = multiprocessing.Pool(processes=10)   # create a pool of 10 processes  

    pool.map(cms_checker, urls)   # map cms_checker function to each url in the list
