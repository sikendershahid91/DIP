class interpolation:
    def linear_interpolation(self, pt1, pt2, unknown):
        """Computes the linear interpolation for the unknown values using pt1 and pt2
        take as input
        pt1: known point pt1 and f(pt1) or intensity value
        pt2: known point pt2 and f(pt2) or intensity value
        unknown: take and unknown location
        return the f(unknown) or intentity at unknown

        pt = (y,x,I) 
        unknown = (y,x)

        """
        #Write your code for linear interpolation here
        x1 = pt1[1]
        x2 = pt2[1]
        x  = unknown[1]
        I1 = pt1[2]
        I2 = pt2[2]

        if x2-x1 == 0 :
            return I1
        else:
            return 1/(x2-x1)*(I1*(x2-x) + I2*(x-x1))

    def bilinear_interpolation(self, pt1, pt2, pt3, pt4, unknown):
        """Computes the linear interpolation for the unknown values using pt1 and pt2
        take as input
        pt1: known point pt1 and f(pt1) or intensity value
        pt2: known point pt2 and f(pt2) or intensity value
        pt1: known point pt3 and f(pt3) or intensity value
        pt2: known point pt4 and f(pt4) or intensity value
        unknown: take and unknown location

        pt = (y,x,I)
        unknown = (y,x)

        return the f(unknown) or intentity at unknown"""

        # Write your code for bilinear interpolation here
        # May be you can reuse or call linear interpolatio method to compute this task
        I1 = self.linear_interpolation(pt1, pt2, unknown)
        I2 = self.linear_interpolation(pt3, pt4, unknown)
        return self.linear_interpolation( (pt1[1],pt1[0], I1),
                                          (pt3[1],pt3[0], I2),
                                          unknown[::-1]) 
