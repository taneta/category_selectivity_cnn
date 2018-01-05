# CNN filters category selectivity

This project helps to understand a CNN's properties: 

- which layer contains filters sensitive to a certain category
- what kind of image categories activate particular filter
- which layer to choose for latent feature extraction for a given category

VGG16 from `keras.applications` is used as a CNN model.


### Prerequisites

Required libraries

```
keras
plotly
ipywidgets
```
### How to:

1. Put your images into a folder, containing subfolders for every category you are interested in.
2. Lauch `category_selectivity.ipynb` to get the activations and measure category selectivity for each filter from chosen layers.
3. Go to `plot_filter_selectivity.ipynb` to visualize the results.


<b><i>Category Selectivity</i></b>

To measure neuron's preferences towards a category, I propose to normalize the neurons responses first and, then, to measure a proportion of activativations related the category:

$$NormalizedActivation = {Activation - min(Activation) \over max(Activation) - min(Activation) + \epsilon}$$

$$CategorySelectivity = {\sum(NormalizedActivation_{category})\over N_{category}$$


## Authors

* **Katerina Malakhova** - [taneta](https://github.com/taneta)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
