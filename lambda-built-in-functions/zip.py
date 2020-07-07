nums1 = [1,2,3,4,5]
nums2 = [2,3,4,5,6]
# creates a tuple
x = zip(nums1, nums2)

# creates a list of tuples
z = list(y)

five_by_two = [(0,1), (1,2), (3,4), (4,5)]

list(zip(* five_by_two))
# creates [(0,1,2,3,4), [1,2,3,4,5]]
# takes the first one from each tuple and it to a new tuple


midterms = [80,91,78]
finals = [98,89,53]
students = ['dan', 'ang', 'kate']


# returns dict with {student:highest score} USING DICT COMP
# {'dan': 98, 'ang': 91, 'kate': 78}
final_grades = {t[0]:max(t[1], t[2]) for t in zip(students, midterms, finals)}


# returns dict with {student:highest score} (same thing as above) USING MAP+LAMBDA
# {'dan': 98, 'ang': 91, 'kate': 78}
final_grades = dict(
	zip(
		students,
		map(
			lambda pair: max(pair),
			zip(midterms, finals)
		)
	)
)

# returns dict with student:average score
# {'dan': 89.0, 'ang': 90.0, 'kate': 65.5}
avg_grades = dict(
	zip(
		students,
		map(
			lambda pair: ((pair[0]+pair[1])/2),
			zip(midterms, finals)
		)
	)
)
