
# coding: utf-8

# In[10]:


def find_prime_until(y):
    x = int(y);
    print("\nPrime Numbers until:")
    for num in range(0, x+1):
            if num>1:
                for i in range(2, num):
                    if(num%i)==0:
                        break;
                else:
                    print(num);
                    
find_prime_until(20)

