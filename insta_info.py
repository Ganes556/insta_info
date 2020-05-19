from bs4 import BeautifulSoup
import requests
def scrapeInstagram(soup1,url):
    data = soup1.find(name="meta",attrs={"property":"og:description"})
    data_info = data['content'].split()
    if '"overall_category_name":null,"is_private":true' in url.text:
        private_or_not = "Private"
    else:
        private_or_not = "Not Private"
   
    return data_info,private_or_not
def output(data,account_name):
    followers = f"{data[0][0]} Followers"
    following = f"{data[0][2]} Following"
    post = f"{data[0][4]} Posts"
    private_or_not = data[1]
    decor([followers,following,post,private_or_not,account_name])
def decor(textnya):
    print("\n"+"-"*12 + f" INFO AKUN {textnya[4]} " + "-"*12 + "\n" \
            f"[+] Followers = {textnya[0]}\n" \
            f"[+] Following = {textnya[1]}\n"\
            f"[+] Post = {textnya[2]}\n"\
            f"\n****Account {textnya[3]}****" 
        )
    
if __name__ == '__main__':
    username_instagram = input("username >> ")
    get_url = requests.get("https://www.instagram.com/"+username_instagram)
    soup1 = BeautifulSoup(get_url.content,"lxml")
    data = scrapeInstagram(soup1,get_url) 
    output(data,username_instagram) 
