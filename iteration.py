# infinite iterators 


# count(start=, step=)
#cycle(iterable)
# repeat(object, time)


from itertools import count
for i in count (10,1):
    if i >=20:
        break
    print(i,end=" ")



#cycle(iterable)

from itertools import cycle
c=0
for item in cycle ([1,2,3,4,5,'sarthak']): # cycle repeat forever if we dont bring it to end..

    print(item)
    c+=1
    if c==6:
        break

#repeat
from itertools import repeat
for i in repeat('hello',5): # (object, times)
    print(i,end=' ')



#chain()
from itertools import chain
print(list(chain([1,2],[4,5,6],[1,3])))    # combine multiple iterables into one..



#accumulate - create runnning totals(prefix sums.)
from itertools import accumulate
print(list(accumulate([1,2,3,4,5]))) #[1,3,6,10,15]- output


# finite iterators 

#accumulate(iterable)
# chain (iterables)- join muliple iterables.
# compress(data, selectors)- file using true/false
# dropwhile(predicate,iterable)- drop until condition become false
#takewhile(predicate,iterble)- opposite of dropwhile.

    
# combinatorics..

from itertools import product
list1=list(product([1,2,23],['sarthak','shawn']))
print(list1) # product of two set..

from itertools import permutations
print(list(permutations([1,2,3]))) # order does not matter..
print(list(permutations([1,2,3],2))) # in how many number of element permutation is required..


# permutation of a string..
print(list(permutations('abc')))
   # to join them..
print([''.join(p) for p in permutations("abc")])
  # if permutation of length is needed
for p in permutations('sarthak',2 ):
    print("".join(p))


# let say we have duplicates value then permutation
print(list(set(permutations([1,23,3,3]))))
#Getting Only Unique Permutations (Better Way)
anokha=set(permutations("aaabbb"))

# Checking if Two Words Are Permutations (Interview)
def per_check(a,b):
    return sorted(a)==sorted(b)


digits = [1,2,3,4]

nums = ["".join(map(str,p)) for p in permutations(digits)]
            # map(str,p) apply the str() to every element in p
print(nums) # ''.join only works on string to convert it in string..



# generators functions- a generator is a function that does not return all values at once instead, it yield values one at a time, only when needed..
def gen_1():
    yield 1 
    yield 2
    yield 3

print(next(gen_1()))



x = [1,2,["Afroz","Sarthak"]]
y=[]

for i in x:
    if isinstance(i,list):
        y.extend(i)
    else:
        y.append(i)
print(y)

   