from datetime import datetime 

'''


-Encapsulation is basically bundling of related attributes and methods to form meanigful blueprint to 
create objects as well as restricting access

-Abstraction is hiding the internal complex implementation and logic of methods from the end users  

-Inheritance is basically creating new sub classes from parent classes to share properties and methods





attribute _email for protected variables, __email for private(mangled names = _classname.__email)
python doesnt have standard or strict access modifiers like private public protected

in cpp protected and private variables cant be accessed outside but in python it can be, and it is the 
dev's duty to seggragate and follow practices (getters/setters) and use the underscore for 
protected and doubleunder for private variables

getters setters can also be used to put some logic along with accessing or setting an attribute's value 
 (logging, regex, check db logic, validations, etc)

"We're all consenting adults here" is a foundational design philosophy coined by Python's creator, 
Guido van Rossum. It means that the language does not strictly enforce data privacy or hide 
object internals. Instead, Python trusts you to use attributes and methods responsibly rather than 
forcing rigid access control like Java or C++

'''
class Person:

	#Class attribute/Static attribuet, not tied to a single instance/object, shared across all objs
	#created only once per class, unlike instance attribs which get created with every obj
	person_count = 0

	#Constructor
	def __init__(self, name, age, email=None):
		self.name = name
		self.age = age
		self._email = email
		# self.email = "djsfndjfn" #if this was there then the setter would get 
		# and the validation would fail, print statement would return None that
		# would get assigned to _email. 
		Person.person_count += 1



	'''Java way of getter and setter methods -------------------------------------
	def get_email(self):
		print(f"Accessed the email from getter method at {datetime.now()}")
		return self._email

	def set_email(self, email):
		self._email = email
		print(f"Updated the email from setter method at {datetime.now()}")
	---------------------------------------------------------------------------'''


	#python way of getter and setter 'properties'----------------------------------
	@property
	def email(self):
		print(f"Accessed the email from getter property at {datetime.now()}")
		return self._email

	@email.setter
	def email(self, email):
		print(f'Updating the email from setter property at {datetime.now()}')
		self._email = email if "@" in email else print("Recheck the email, not updating...")
		#return self._email #this gets ignored, setters can't return 
	#-------------------------------------------------------------------------------

		
	# Protected instance method(by convention not rule)
	def _is_person_alive(self):
		return self.age > -1

	# Private instance method
	def __is_person_with_online_footprint(self):
		return True if self._email != None else False

	# Instance method	
	def personAnalysis(self):
		life_status = "alive" if self._is_person_alive() else "dead" 
		digital_footprint = "have" if self.__is_person_with_online_footprint() else "do not have"
		print(f"Hi there! I'm {self.name}, and {self.age} years old.\nSo basically I'm {life_status}. Also I {digital_footprint} a digital_footprint.")


	# Static method
	@staticmethod
	def is_valid_voter(p: Person):
		return p.age >= 18








p1 = Person("Babu", -1, "abc@ashd.com")
p2 = Person("Taatya", 56, "tatya@mh.com")
p3 = Person("Ramu", 16)
print(f"{p1.name}'s age is {p1.age}")

'''
==============================================
example of normal way to access and set values of protected properties but should not be done

print(p1._email) 			#can be done but should not be done
p1._email = "babu@babu.com" #can be done but should not be done

==============================================
example of getter and setter method, the java way of doing stuff

print(p1.get_email())
print(p1.set_email("babu@babu.com"))

==============================================
exmaples of getter and setter properties, the python way of doing stuff 
'''


p1.email = "babaua@sdlsd.com"  	#setter property
print(p1.email)					#getter property


print(p2.person_count, p1.person_count, Person.person_count)					#Static/Class property
print(Person.is_valid_voter(p1), p2.is_valid_voter(p1), p2.is_valid_voter(p2))	#Static/Class Method

#p1._is_person_alive() 					#can work but should not be used
#p1.__is_person_with_online_footprint()  #will not work due to mangled name but p1._Person__is_person_with_online_footprint() will work but should not be used 
p1.personAnalysis()
