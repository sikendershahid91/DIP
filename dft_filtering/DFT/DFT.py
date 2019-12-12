# For this part of the assignment, please implement your own code for all computations,
# Do not use inbuilt functions like fft from either numpy, opencv or other libraries

from numpy import exp, pi, zeros

class DFT:

    def forward_transform(self, matrix):
        """Computes the forward Fourier transform of the input matrix
        takes as input:
        matrix: a 2d matrix
        returns a complex matrix representing fourier transform"""
        print(type(matrix), '<<<<<<')

        # matrix[r][c] --> matrix[y][x]
        # (u,v) <- (x,y) -> (c,r)
        
        _matrix = zeros(matrix.shape, dtype=complex)
        K, L = matrix.shape[0] , matrix.shape[1]
        
        for v in range(0,matrix.shape[0]):
            for u in range(0, matrix.shape[1]):
                _sum = 0
                for y in range(0, matrix.shape[0]):
                    for x in range(0, matrix.shape[1]):
                        _sum += matrix[y,x] * \
                                exp( -1j*2*pi*( (u*x/L) + (v*y/K) ) )
                _matrix[v,u] = (( 1 / (K*L) )+0j) * _sum

        return _matrix

    def inverse_transform(self, matrix):
        """Computes the inverse Fourier transform of the input matrix
        matrix: a 2d matrix (DFT) usually complex
        takes as input:
        returns a complex matrix representing the inverse fourier transform"""

        _matrix = zeros(matrix.shape, dtype=complex)
        K, L = matrix.shape[0], matrix.shape[1]

        for v in range(0, matrix.shape[0]):
            for u in range(0, matrix.shape[1]):
                _sum = 0
                for y in range(0, matrix.shape[0]):
                    for x in range(0, matrix.shape[1]):
                        _sum += matrix[y,x] * \
                                exp( 1j*2*pi*( (u*x/L) + (v*y/K) ) )
                _matrix[v,u] = _sum


        return _matrix

    def magnitude(self, matrix):
        """Computes the magnitude of the DFT
        takes as input:
        matrix: a 2d matrix
        returns a matrix representing magnitude of the dft"""

        from numpy import sqrt
        
        for v in range(0, matrix.shape[0]):
            for u in range(0, matrix.shape[1]):
                matrix[v,u] = sqrt( (matrix[v,u].real)**2 + (matrix[v,u].imag)**2 )

        return matrix

    def discrete_cosine_tranform(self, matrix):
        """Computes the discrete cosine transform of the input matrix
        takes as input:
        matrix: a 2d matrix
        returns a matrix representing discrete cosine transform"""

        from numpy import cos, sin
        
        _matrix = zeros(matrix.shape, dtype=complex)
        K, L = matrix.shape[0], matrix.shape[1]

        for v in range(0, matrix.shape[0]):
            for u in range(0, matrix.shape[1]):
                _sum = 0
                for y in range(0, matrix.shape[0]):
                    for x in range(0, matrix.shape[1]):
                        _sum += matrix[y,x] * \
                                cos( (pi/L)*(x+0.5)*u ) * \
                                cos( (pi/K)*(y+0.5)*v ) 
                _matrix[v,u] = _sum

        return _matrix
