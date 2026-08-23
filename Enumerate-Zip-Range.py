names = ['anurag', 'atharva', 'omkar']
marks = [10,32,23,23]

for i, y in enumerate(zip(names, marks), start=1):
	print(f'#{i} - {y[0]}, {y[1]}')


'''
#1 - anurag, 10
#2 - atharva, 32
#3 - omkar, 23
'''

'''
U would use enumerate instead of range in cases where u just need the ordering and basic index
of the iterables. Use range when u need to do some complex operations(i++, i--) or to make
changes in place in the list on the given indexes.

If you just want to know the positioning of the elements, go with enumerate, like in the 
two sum problem


U can sort list of lists/iterables in python on specific indexes with th lambda key function
sorted() vs .sort()

sorted(data, key=lambda x: x[0])  # returns new list, original unchanged
data.sort(key=lambda x: x[0])     # sorts in place, returns None

'''

