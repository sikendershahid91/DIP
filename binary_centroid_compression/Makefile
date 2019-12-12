
all:
	@echo "Usage:"
	@echo "\tmake cells"
	@echo "\tmake clean"
	@echo "\tmake clean_all_output"

cells:
	./dip_hw2_region_analysis.py -i cells.png

clean:
	@echo "Cleaning project"
	@find . -name "__pycache__" | xargs rm -rf ;
	@find . -name "*~" | xargs rm -f ;
	@find . -name ".#*" | xargs rm -f ; 
	@find . -name "#*#" | xargs rm -f ;

clean_all_output:
	@echo "removing files from output directory"
	@rm output/cellct/*.jpg \
	output/cellct/*.png \
	output/Compression/*.jpg
