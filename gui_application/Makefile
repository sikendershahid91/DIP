
all:
	@echo "Usage:"
	@echo "\tmake project " 
	@echo "\tmake clean   "
	@echo "\tmake filter : test"

project:
	python3 src/main.py 

filter:
	cd test && python3 slicing_test.py

clean:
	@echo "Cleaning project"
	@find . -name "__pycache__" | xargs rm -rf ;
	@find . -name "*~" | xargs rm -f ;
	@find . -name ".#*" | xargs rm -f ; 
	@find . -name "#*#" | xargs rm -f ;
