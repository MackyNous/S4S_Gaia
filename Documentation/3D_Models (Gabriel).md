# 3D Models
@Maricio

As we were reverse engineering Gaia Sky we found out that there are several 3D models of spacechips already in Gaia. After doing some research this had been confirmed to us by the oficial website itself that shows the following image: 


![Screenshot of enterprise](https://raw.githubusercontent.com/MackyNous/S4S_Gaia/Documentation/Documentation/img/3D_model.PNG)


As can be seen, the enterprise from star trek can be found in Gaia Sky. And ofcourse we wanted this too, so after searching and reading we found out we should edit the 'satellites.json' file as follows: 


```javascript

	{
		"name" : "Enterprise",
		"wikiname" : "Enterprise",
		"color" : [0.3, 0.5, 0.9, 1.0],
		// in Km
		"size" : 0.9,
		"ct" : Satellites,
		
		"parent" : "Earth",
		"impl" : "gaia.cu9.ari.gaiaorbit.scenegraph.GenericSpacecraft",
		
		"coordinates" : {
					// This must implement gaia.cu9.ari.gaiaorbit.util.coord.IBodyCoordinates				
					"impl" : "gaia.cu9.ari.gaiaorbit.util.coord.StaticParentRotationCoordinates",
					"position" : [0.0, 7000, 0.0]
					},
		"parentorientation" : True,
		"hidden" : False,
		"renderquad" : False,
		
		"model"	: {
				"args" : [true],
				"usecolor" : False,
				"model" : "data/models/usse/usse.obj"
			},
		
		"shadowvalues" : [ 0.0, 0.0, 0.0 ]
		
		}

```


After saving and relaunching the Gaia Sky we were able to load this 3D_Model. In theory this is possible for every 3D model in a obj format. So if we wanted to (for example) have the ISS in the sky, this is a possibility too.
