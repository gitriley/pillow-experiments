from PIL import Image
import os
import sys
'''
truths/variables...

newImage size...(e.g. 1500,1500)...should be 2x the smallest image, then cropped to square?
inputImage1 size
inputImage2 size
should the splice bars be vertical or horizontal 
slice-width: 

step through at intervals of 'slice-width', i.e. increase slice/crop coordinates 
by 'slice-width' with each loop
continue while inputImage1 and inputImage2 slice coordinates > smallest inputImage's width or height
	(if slicing vertical bars, stop at smallest inputImage's width, if )

'''

def combine(img1, img2, sliceWidth, direction):
	if direction == 'vertical':
		return combineVertical(img1, img2, sliceWidth)
	elif direction == 'horizontal':
		return combineHorizontal(img1, img2, sliceWidth)



def combineExpandedVertical(img1, img2, sliceWidth):
	smallestHeight = smallestH(img1, img2)
	smallestWidth = smallestW(img1, img2)

	print(img1.size)
	print(img2.size)	

	#sliceLocation = sliceWidth
	sliceStart = 0
	sliceEnd = sliceWidth
	slice = (sliceStart, 0, sliceEnd, smallestHeight)

	img1PasteLocation = (0, 0)
	img2PasteLocation = (sliceWidth, 0)

	result = Image.new("RGB",(2*smallestWidth, smallestHeight))

	while (slice[2] < (2*smallestWidth)):
		img1_slice = img1.crop(slice)
		img2_slice = img2.crop(slice)
		result.paste(img1_slice, img1PasteLocation)

		result.paste(img2_slice, img2PasteLocation)

		img1PasteLocation = (img1PasteLocation[0]+(2*sliceWidth), 0)
		img2PasteLocation = (img2PasteLocation[0]+(2*sliceWidth), 0)


		sliceStart = slice[0] + sliceWidth
		sliceEnd = slice[2] + sliceWidth
		slice = (sliceStart, 0, sliceEnd, smallestHeight)

	return result

def combineVertical(img1, img2, sliceWidth):
	smallestHeight = smallestH(img1, img2)
	smallestWidth = smallestW(img1, img2)	

	sliceStart = 0
	sliceEnd = sliceWidth
	slice = (sliceStart, 0, sliceEnd, smallestHeight)

	pasteLocation = (0, 0)
	#img2PasteLocation = (sliceWidth, 0)
	pasteNext = 'img1'

	result = Image.new("RGB",(smallestWidth, smallestHeight))

	while (slice[0] < smallestWidth):
		if pasteNext == 'img1':
			img1_slice = img1.crop(slice)
			result.paste(img1_slice, pasteLocation)
			pasteNext = 'img2'
		elif pasteNext == 'img2':
			img2_slice = img2.crop(slice)
			result.paste(img2_slice, pasteLocation)
			pasteNext = 'img1'

		pasteLocation = (pasteLocation[0]+sliceWidth, 0)


		sliceStart = slice[0] + sliceWidth
		sliceEnd = slice[2] + sliceWidth
		slice = (sliceStart, 0, sliceEnd, smallestHeight)

	return result

def combineHorizontal(img1, img2, sliceWidth):
	smallestHeight = smallestH(img1, img2)
	smallestWidth = smallestW(img1, img2)

	#slice = (0, 0, smallestWidth, sliceWidth)	

	#sliceLocation = sliceWidth
	sliceStart = 0
	sliceEnd = sliceWidth
	slice = (0, sliceStart, smallestWidth, sliceEnd)

	pasteLocation = (0, 0)
	#img2PasteLocation = (sliceWidth, 0)
	pasteNext = 'img1'

	result = Image.new("RGB",(smallestWidth, smallestHeight))

	while (slice[1] < smallestHeight):
		img1_slice = img1.crop(slice)
		img2_slice = img2.crop(slice)
		if pasteNext == 'img1':
			result.paste(img1_slice, pasteLocation)
			pasteNext = 'img2'
		elif pasteNext == 'img2':
			result.paste(img2_slice, pasteLocation)
			pasteNext = 'img1'

		pasteLocation = (0, pasteLocation[1]+sliceWidth)


		sliceStart = slice[1] + sliceWidth
		sliceEnd = slice[3] + sliceWidth
		slice = 0, sliceStart, smallestWidth, sliceEnd

	return result


def smallestH(img1, img2):
	if img1.height < img2.height:
		return img1.height
	else:
		return img2.height


def smallestW(img1, img2):
	if img1.width < img2.width:
		return img1.width
	else:
		return img2.width

im1 = Image.open(sys.argv[1])
im2 = Image.open(sys.argv[2])


combo = combine(im1, im2, int(sys.argv[3]), sys.argv[4])

combo.show()

if len(sys.argv) == 6 and sys.argv[5] == 'save':
	import time
	combo.save('output_{}.png'.format(int(time.time())))

