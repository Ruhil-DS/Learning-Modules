data = "/Users/pushpakruhil/IIT-M CODING/Hashcode/input_data/a_an_example.in.txt"

likes = {}
dislikes = {}
clients = None

def parse_input(data):
    l = []
    with open(data, "r") as f:
        clients = int(f.readline())
        if clients != "":
            for i in range(1, 2*clients + 1):

                line = f.readline()
                temp = line.split()
                for j in range(1, int(temp[0])+1):
                    print(temp[j])
                print("-----")





print(parse_input(data))
