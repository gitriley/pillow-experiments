from PIL import Image
import os
import sys

def combine(img1, img2, sliceWidth, direction):
	if direction == 'vertical':
		return combineVertical(img1, img2, sliceWidth)
	elif direction == 'horizontal':
		return combineHorizontal(img1, img2, sliceWidth)


def combineVertical(img1, img2, sliceWidth):
	smallestHeight = smallestH(img1, img2)
	smallestWidth = smallestW(img1, img2)	

	sliceStart = 0
	sliceEnd = sliceWidth
	slice = (sliceStart, 0, sliceEnd, smallestHeight)

	pasteLocation = (0, 0)
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


	sliceStart = 0
	sliceEnd = sliceWidth
	slice = (0, sliceStart, smallestWidth, sliceEnd)

	pasteLocation = (0, 0)
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


