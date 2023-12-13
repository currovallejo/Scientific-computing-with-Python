import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        if not kwargs:
            raise ValueError("At least one ball is required.")
        self.colors = kwargs
        self.contents=[]
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(str(key))
    
    def draw(self, n_to_draw):
        random_balls=[]
        self.contents.copy()
        if n_to_draw >= len(self.contents):
            return self.contents
        else:
            for i in range(n_to_draw):
                random_ball = random.choice(self.contents)
                self.contents.remove(random_ball)
                random_balls.append(random_ball)
            # print('el numero de items en self.contents es: ', len(self.contents))
            return random_balls
    
    def clone(self):
        return Hat(**self.colors)
        
        


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M=0
    for i in range(num_experiments):
        copied_hat = hat.clone()
        # print('**** Experimento Nº %s ****' %i)
        # print('contenido de hat: ', hat.contents)
        # print('contenido de copied_hat ', copied_hat.contents)
        balls_drawn=[]
        balls_drawn = copied_hat.draw(num_balls_drawn).copy() # lista de strings
        # print('bolas robadas = balls_drawn: ', balls_drawn)
        expected_balls_list = []
        for key, value in expected_balls.items():
            for i in range(value):
                expected_balls_list.append(str(key))
        # print('se quiere calcular la P(X) de estas bolas: ', expected_balls_list)

        total_iguales = 0
        for i,color1 in enumerate(expected_balls_list):
            # print(f"Outer loop iteration {i}")
            for j,color2 in enumerate(balls_drawn):
                # print(f"  Inner loop iteration {j}")
                if color1==color2:
                    total_iguales += 1
                    balls_drawn.remove(color1)
                    # print('1 bola de color **%s** coincide con lo que buscamos, la quitamos' %color1)
                    # print('bolas extraídas a comparar ahora: ', balls_drawn)
                    # print("  Breaking out of the inner loop")
                    break
                    
             
        
        if total_iguales >= len(expected_balls_list):
            M+= 1
    print('Nº de experimentos satisfactorios: %s' %M)
    print('M vale : ', M)
    print(' el numero de experimentos total es: ', num_experiments)
    # print(len(expected_balls_list))
    
    Probability =M/num_experiments
    return Probability
