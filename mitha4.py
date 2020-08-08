source_url = 'http://cdn8.openculture.com/wp-content/uploads/2014/04/Chaplin-Charlie-His-New-Job_011.jpg' #@param {type:"string"}
render_factor = 35  #@param {type: "slider", min: 7, max: 40}
watermarked = False #@param {type:"boolean"}

if source_url is not None and source_url !='':
    image_path = colorizer.plot_transformed_image_from_url(url=source_url, render_factor=render_factor, compare=True, watermarked=watermarked)
    
else:
    print('Provide an image url and try again.')
