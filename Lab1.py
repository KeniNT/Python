import os


class Review:
    def __init__(self, custID, prodID, revdate, revrate, revtext):
        self.custID=custID
        self.prodID=prodID
        self.revdate=revdate
        self.revrate=revrate
        self.revtext=revtext
        
invalid=0
valid=0

def read_all_reviews(file):
    global invalid, valid
    revlist=[]
    with open(file, 'r') as f:
        for line in f:
            data=line.strip().split(" ",4) #Five splits atmost possible
            if len(data)==5:
                custID,prodID,revdate,revrate,revtext=data
                try:
                    review=Review(custID,prodID,revdate,int(revrate),revtext)
                    revlist.append(review)
                    valid+=1
                except ValueError:
                    invalid+=1
            else:
                invalid+=1
    return revlist


def cal_avg_rating(revlist):
    avg_rating={} 
    product_rating={}
    
    for review in revlist:
        if review.prodID not in product_rating:
            product_rating[review.prodID]=[]
        product_rating[review.prodID].append(review.revrate)
    avg_rating={productID:sum(rating)/len(rating) for productID, rating in product_rating.items()}
    return avg_rating

all_rev=[]
filelist=os.listdir('C:\sem5\Adv_Python_Lab')
for file in filelist:
    if file.endswith('.txt'):
        revlist=read_all_reviews(file)
        all_rev.extend(revlist)

average=cal_avg_rating(all_rev)

prod_avg_rate={x:y for x, y in sorted(average.items(), key=lambda item:item[1], reverse=True)}
e='Keni Tandel 22BCP392\n'
a='Total reviews: ' + str((valid+invalid)) + '\n'
b='Total valid reviews: ' + str(valid) + '\n'
c='Total invalid reviews: ' + str(invalid) + '\n'
d='Top 3 products: ' + '\n'

par=list(prod_avg_rate.items())[:3]              

with open('Survey.txt','w') as s:
                s.writelines([e,a,b,c,d])
                for x,y in par:
                    s.write('Product ID: '+str(x)+' Average rating: '+str(y)+'\n')
