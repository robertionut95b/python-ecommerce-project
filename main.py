import pandas as pd
import requests
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt

# vrt_data = [{"product_name": "ski", "product_value": 100}, {"product_name": "jacket", "product_value": 153}]
vrt_data = []
vrt_url = "https://www.6pm.com/girls-boots/CK_XARCz1wHAAQPiAgMBAhg.zso?s=isNew%2Fdesc%2FgoLiveDate%2Fdesc%2FrecentSalesStyle%2Fdesc%2F&si=4950129&sy=1&pf_rd_r=77C6019488D54B2199A9&pf_rd_p=f8d61d8f-f682-48dc-9dce-9c423af55b6c"


def retrieve_data(url=vrt_url):
    vrt_resp = requests.get(url)
    if vrt_resp.status_code != 200:
        print(f"Could not retrieve data from {url}")
        return

    vrt_soup = BeautifulSoup(vrt_resp.content, 'html.parser')
    vrt_articles = vrt_soup.find_all("article", {"class": "sr-z"})

    vrt_list = []
    for vrt_item in vrt_articles:
        vrt_title_elem = vrt_item.find("dd", {"class": "Ep-z"})
        vrt_price_elem = vrt_item.find("span", {"class": "Gr-z"})

        vrt_title = vrt_title_elem.string
        vrt_price = float(vrt_price_elem.get("content"))

        vrt_list.append({"product_name": vrt_title, "product_value": vrt_price})

    print("Fetched data")
    return vrt_list


def chart_data(data):
    vrt_products = [elem.get("product_name") for elem in data]
    vrt_values = [elem.get("product_value") for elem in data]

    vrt_fig = plt.figure(figsize=(10, 5))
    plt.bar(vrt_products, vrt_values, color="maroon", width=0.2)

    plt.xlabel("Products")
    plt.xticks(rotation="vertical")
    plt.ylabel("Price")
    plt.title("Products and their prices")

    plt.show()


def data_to_pd(data):
    return pd.DataFrame(data)


def print_matrix(data):
    vrt_matx = data_to_pd(data).values
    print(vrt_matx)
    return vrt_matx


def save_to_excel(data, fn="data.xlsx"):
    df = data_to_pd(data)
    return df.to_excel(fn)


def main():
    print("############ Welcome ############")
    print("Select your option to continue")
    print("1. Retrieve data")
    print("2. Create the graph")
    print("3. Display the matrix")
    print("4. Save to Excel file")
    print("5. Exit")

    while True:
        print("\nEnter your option ...\n")
        vrt_opt = int(input())
        if vrt_opt in [1, 2, 3, 4, 5]:
            print(f"Chosen option {vrt_opt}")
        else:
            print("Unknown option. Please try again")

        if vrt_opt == 1:
            vrt_lst = retrieve_data()
            vrt_data.extend(vrt_lst)

        if vrt_opt == 2:
            chart_data(vrt_data)

        if vrt_opt == 3:
            print_matrix(vrt_data)

        if vrt_opt == 4:
            save_to_excel(vrt_data)
            print("File saved")

        if vrt_opt == 5:
            print("Exiting ...")
            break


if __name__ == '__main__':
    main()
