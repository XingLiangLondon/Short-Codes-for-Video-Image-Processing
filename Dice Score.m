A = imread('B-uniform01.bmp');
I = rgb2gray(A);
figure
imshow(I)
title('Original Image')
mask = false(size(I));
mask(25:end-25,25:end-25) = true;
BW = activecontour(I, mask, 300);
imshow(BW)
BW_groundTruth = imread('B-uniform01_groundtruth.bmp');
imshow(BW_groundTruth)
dice = 2*nnz(BW&BW_groundTruth)/(nnz(BW) + nnz(BW_groundTruth));
similarity = dice;
imshowpair(BW, BW_groundTruth)
title(['Dice Index = ' num2str(similarity)])
