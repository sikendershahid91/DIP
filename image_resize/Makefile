
all:
	@echo "Usage:"
	@echo "\tmake cell1"
	@echo "\tmake cell2"
	@echo "\tmake clean"
	@echo "\tmake clean_all_output"

cell1:
	./dip_hw1_resize.py -i cells.png -fx 1.5 -fy 1.5 -m nearest_neighbor
	./dip_hw1_resize.py -i cells.png -fx 1.5 -fy 1.5 -m bilinear
	./dip_hw1_resize.py -i cells.png -fx 0.5 -fy 0.5 -m nearest_neighbor
	./dip_hw1_resize.py -i cells.png -fx 0.5 -fy 0.5 -m bilinear
	./dip_hw1_resize.py -i cells.png -fx 3 -fy 3 -m nearest_neighbor
	./dip_hw1_resize.py -i cells.png -fx 3 -fy 3 -m bilinear
	./dip_hw1_resize.py -i cells.png -fx 4 -fy 4 -m nearest_neighbor
	./dip_hw1_resize.py -i cells.png -fx 4 -fy 4 -m bilinear

cell2:
	./dip_hw1_resize.py -i cell2.jpg -fx 1.5 -fy 1.5 -m nearest_neighbor
	./dip_hw1_resize.py -i cell2.jpg -fx 1.5 -fy 1.5 -m bilinear
	./dip_hw1_resize.py -i cell2.jpg -fx 0.5 -fy 0.5 -m nearest_neighbor
	./dip_hw1_resize.py -i cell2.jpg -fx 0.5 -fy 0.5 -m bilinear
	./dip_hw1_resize.py -i cell2.jpg -fx 3 -fy 3 -m nearest_neighbor
	./dip_hw1_resize.py -i cell2.jpg -fx 3 -fy 3 -m bilinear
	./dip_hw1_resize.py -i cell2.jpg -fx 4 -fy 4 -m nearest_neighbor
	./dip_hw1_resize.py -i cell2.jpg -fx 4 -fy 4 -m bilinear
clean:
	@echo "Cleaning project"
	@find . -name "__pycache__" | xargs rm -rf ;
	@find . -name "*~" | xargs rm -f ;
	@find . -name ".#*" | xargs rm -f ; 
	@find . -name "#*#" | xargs rm -f ;

clean_all_output:
	@echo "removing files from output directory"
	@rm output/resize/cell*
