import json
from pprint import pprint


def main():
    
    with open("data.json","r") as json_file:
        data = json.load(json_file)

        print(data[0]['last_name'])
        pprint(data)



def main_write_json():
    with open('MOCK_DATA.csv','r') as csv_file:
        # content = csv_file.read()
        # print(content.splitlines())
        # content = csv_file.readlines()
        # print(content)
        # content = csv_file.readlines()
        # h = content[0]
        # d = content[1:]
        h = next(csv_file)
        k = h.strip().split(',') 
        print(k) # [id,first_name,last_name,email,gender,ip_address]
        rows = []
        for line in csv_file:
            line_data = line.strip().split(',') # [1,Armstrong,Markos,amarkos0@hao123.com,Male,51.232.180.172]
            d= dict(zip(k,line_data))
            # V1
            # for i,cell in enumerate(line_data):
            #     the_key =  k[i]
            #      d[the_key] = cell
            rows.append(d)

    with open("data.json","w") as json_file:
        json.dump(rows,json_file,indent=4)
        #s = json.dumps(rows,json_file,indent=4)


if __name__=='__main__':
    main()
