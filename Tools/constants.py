class HSV_ranges:
    """
    HSV ranges of objects that we want to track
    """
    class Powercell:
        """
        Contains the HSV ranges of the powercell 
        TODO change the HSV ranges to the front camera
        """
        lowH = 22
        lowS = 115
        lowV = 80

        highH = 38
        highS = 242
        highV = 255
    
        low = (lowH, lowS, lowV)
        high = (highH, highS, highV)


class Cameras:
    """
    Information about cameras
    TODO add the front camera
    """
    class LIFECAM_3000:
        """
        Information about our back camera who tracks the reflective tapes
        """
        focal_length = 697.0395744431028
        fov = 24.227745318014267895
        mid_x = 640
        mid_y = 360