import pandas as pd


class DataUnits(pd.DataFrame):


    _metadata = ['units']      #setting up the metadata, i.e units


    


    def __init__(self, *args, **kwargs):                       #initializing the object
        self.units = pd.Series(kwargs.pop("units", None))      #setting the units of the object
        super().__init__(*args, **kwargs)            #calling the init function of super class, i.e. pandas Dataframe

 
    def copy_data_unit(self):                                  #functio for creating copy of current DataUnits object 
        copy = DataUnits(self)                                 # Creating copy
        copy.units = self.units                                # assiging units to the copied object
        return copy                                             #returning the copied object to the called function
    def ret_all_units(self):
    	return self.units


    def get_data_unit(self, attr):                              #function for getting the unit of a given attribute
        attr_list=[]                                            #creating a list of columns of the object
        for i in self.columns:
        	attr_list.append(i)                                 #apending the attributes in attr_list
        index = attr_list.index(attr)                           # and finding the index of the attribute
        print(index)
        print(self.units)
        print(len(self.units) )
        if len(self.units) > max (0 ,index) :                      
            if len (self.units[index]) > 0 :
                return self.units[index]
            else :
                print("Attribute  Not set!!!!" )
        else :
            print("Attribute Not set!!!" )

"""
Test 
"""




    
