
all:
	@echo "Usage:"
	@echo "\tmake dft"
	@echo "\tmake lenna"
	@echo "\tmake lenna0"
	@echo "\tmake all_lenna"
	@echo "\tmake all_lenna0"
	@echo "\tmake clean"
	@echo "\tmake clean_all_output"

dft:
	./dip_hw3_dft.py --fixed

lenna:
	./dip_hw3_filter.py -i Lenna.png -m ideal_l -c 50

lenna0:
	./dip_hw3_filter.py -i Lenna0.jpg -m ideal_l -c 50

all_lenna:
	./dip_hw3_filter.py -i Lenna.png -m ideal_l -c 125
	./dip_hw3_filter.py -i Lenna.png -m butterworth_l -c 125 -o 2
	./dip_hw3_filter.py -i Lenna.png -m gaussian_l -c 125
	./dip_hw3_filter.py -i Lenna.png -m ideal_h -c 125
	./dip_hw3_filter.py -i Lenna.png -m butterworth_h -c 125 -o 2
	./dip_hw3_filter.py -i Lenna.png -m gaussian_h -c 125

all_lenna0:
	./dip_hw3_filter.py -i Lenna0.jpg -m ideal_l -c 75	
	./dip_hw3_filter.py -i Lenna0.jpg -m butterworth_l -c 75 -o 2
	./dip_hw3_filter.py -i Lenna0.jpg -m gaussian_l -c 75
	./dip_hw3_filter.py -i Lenna0.jpg -m ideal_h -c 75	
	./dip_hw3_filter.py -i Lenna0.jpg -m butterworth_h -c 75 -o 2
	./dip_hw3_filter.py -i Lenna0.jpg -m gaussian_h -c 75

clean:
	@echo "Cleaning project"
	@find . -name "__pycache__" | xargs rm -rf ;
	@find . -name "*~" | xargs rm -f ;
	@find . -name ".#*" | xargs rm -f ; 
	@find . -name "#*#" | xargs rm -f ;

clean_all_output:
	@echo "removing files from output directory"
	@rm output/*.jpg
