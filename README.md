# Identifying Saliency in Image using Edge Detection
A new topic in computer vision research right now is Salient Object Detection (SOD) which separates the dominant/prominent item (first item visible to the human eye) from the background. This property automatically recognises and segregates major visual regions resulting in many applications. 

Even though humans distinguish salient objects through boundaries, edge detection and saliency are still two spheres that do not converge. In a Neural Network, the features do not merge well since edges and surfaces do not coincide, one feature represents a surface and the other indicates boundaries between various regions. The primary goal here is providing a mechanism for merging edges with saliency maps to increase saliency performance. 

# Methodology
I suggest an approach that combines saliency and edge detection models. Edge detection ensures that the borders are clear, unlike in other spatial space images, and the given model will separate out and accent the object in the image rather than returning all n of the image's edges. By distinguishing between various pixel types, this can also contribute to image segmentation (strong, weak and non-relevant). Because it creates incredibly thin and crisp lines, we apply canny edge detection. Although the edges detected by other popular edge detection algorithms are detectable too, they are comparatively less than those processed by the Canny edge detector

