import random
from manim import*

class fagnano(Scene):
    def construct(self):
        #First Rectangle
        rect = Rectangle()
        self.play(Create(rect))
        self.play(rect.animate.shift(2*DOWN, 0.5*RIGHT), run_time = 1.4)
        self.wait
        
        rect1_dr_corner = rect.get_corner(direction=DR)
        rect1_dl_corner = rect.get_corner(direction=DL)
        rect1_ul_corner = rect.get_corner(direction=UL)
        rect1_ur_corner = rect.get_corner(direction=UR)
        
        #Line of reflection
        reflection_line_start = [rect1_dr_corner[0], rect1_dr_corner[1]-1.5, 0]
        reflection_line_end = [rect1_dr_corner[0], rect1_ur_corner[1]+1.5, 0]
        l = DashedLine(start = reflection_line_start, 
                        end = reflection_line_end,
                        color = color.RED)
        self.play(Create(l, run_time = 1.6))
        
        #Second Rectangle
        rect_2 = Rectangle().shift(2*DOWN, 0.5*RIGHT)
        self.play(Create(rect_2))
        #second rect shift
        rect_2_shift = abs(rect1_dl_corner[0] - rect1_dr_corner[0])
        self.play(rect_2.animate.shift(rect_2_shift*RIGHT))
        
        #line of reflection vertcial shift
        l_shift_vert = 0.5*abs(rect1_ur_corner[1] - rect1_dr_corner[1])
        self.play(l.animate.shift(l_shift_vert*UP))
        self.play(l.animate.rotate(PI/2))
        
        #Third Rectangle
        rect_3 = Rectangle().shift(2*DOWN, 0.5*RIGHT)
        self.play(Create(rect_3))
        #third rect shift
        rect_3_shift = abs(rect1_dr_corner[1] - rect1_ur_corner[1])
        self.play(rect_3.animate.shift(rect_3_shift*UP))
        
        #line of reflection horizontal shift
        l_shift_horiz = abs(rect1_ur_corner[0] - rect1_ul_corner[0])
        self.play(l.animate.shift(l_shift_horiz*LEFT))
        self.play(l.animate.rotate(3*PI/2))

        #Fourth Rectangle
        rect_4 = Rectangle().shift(2*DOWN, 0.5*RIGHT)
        rect_4.shift(rect_3_shift*UP)
        self.play(Create(rect_4))
        #fourth rect shift
        self.play(rect_4.animate.shift(rect_2_shift*LEFT))
        
        #Random Points on the rectangle
        dot_radius = 0.1
        dot_color = color.PINK

        
        vec1 = [random.uniform(rect1_dl_corner[0]+0.3, rect1_dr_corner[0]-0.3), rect1_dl_corner[1], 0] #bottom edge point
        vec2 = [rect1_ur_corner[0], random.uniform(rect1_dr_corner[1]+0.2, rect1_ur_corner[1]-0.2), 0] #right edge point
        vec3 = [random.uniform(rect1_ul_corner[0]+0.3, rect1_ur_corner[0]-0.3), rect1_ul_corner[1], 0] #top edge point
        vec4 = [rect1_ul_corner[0], random.uniform(rect1_dr_corner[1]+0.2, rect1_ur_corner[1]-0.2), 0] #left edge point
        
        #polygon rand_points on perimeter
        point1 = Dot(color=dot_color, point=vec1, radius=dot_radius) #bottom edge point
        point2 = Dot(color=dot_color, point=vec2, radius=dot_radius) #right edge point
        point3 = Dot(color=dot_color, point=vec3, radius=dot_radius) #top edge point
        point4 = Dot(color=dot_color, point=vec4, radius=dot_radius) #left edge point
        self.play(Create(point1), Create(point2), Create(point3), Create(point4))

        self.play(l.animate.shift(abs(rect1_dl_corner[0] - rect1_dr_corner[0])*RIGHT,
                                    0.5*abs(rect1_dr_corner[1] - rect1_ur_corner[1])*DOWN))
        
        
        #poly_2 rand_points on perimeter
        point1_rect2 = Dot(color=dot_color, point=vec1, radius=dot_radius) #bottom edge point on rect2
        #point2_rect2 = Dot(color=dot_color, point=vec2, radius=dot_radius) #right edge point on rect2
        point3_rect2 = Dot(color=dot_color, point=vec3, radius=dot_radius) #top edge point on rect2
        point4_rect2 = Dot(color=dot_color, point=vec4, radius=dot_radius) #left edge point on rect2
        self.play(Create(point1_rect2), Create(point3_rect2), Create(point4_rect2)) #, Create(point2_rect2)
        #reflection shift
        point1_rect2_shift = 2*abs(point1_rect2.get_center()[0] - rect1_dr_corner[0]) 
        point3_rect2_shift = 2*abs(point3_rect2.get_center()[0] - rect1_ur_corner[0]) 
        point4_rect2_shift = 2*abs(point4_rect2.get_center()[0] - rect1_ur_corner[0]) 
        self.play(
            point1_rect2.animate.shift(point1_rect2_shift*RIGHT),
            point3_rect2.animate.shift(point3_rect2_shift*RIGHT),
            point4_rect2.animate.shift(point4_rect2_shift*RIGHT)
        )
        
        self.play(l.animate.shift(l_shift_vert*UP))
        self.play(l.animate.rotate(PI/2))

        #poly_3 rand_points on perimeter
        point1_rect3 = Dot(color=dot_color, point=vec1, radius=dot_radius) #bottom edge point on rect3
        point2_rect3 = Dot(color=dot_color, point=vec2, radius=dot_radius) #right edge point on rect3
        #point3_rect3 = Dot(color=dot_color, point=vec3, radius=dot_radius) #top edge point on rect3
        point4_rect3 = Dot(color=dot_color, point=vec4, radius=dot_radius) #left edge point on rect3
       
        self.play(Create(point1_rect3), Create(point2_rect3), Create(point4_rect3)) #, Create(point3_rect3)
        #reflection shift
        point1_rect3_shift = 2*abs(point1_rect3.get_center()[1] - rect1_ur_corner[1]) 
        point2_rect3_shift = 2*abs(point2_rect3.get_center()[1] - rect1_ur_corner[1]) 
        point4_rect3_shift = 2*abs(point4_rect3.get_center()[1] - rect1_ul_corner[1]) 
        self.play(
            point1_rect3.animate.shift(point1_rect3_shift*UP),
            point2_rect3.animate.shift(point2_rect3_shift*UP),
            point4_rect3.animate.shift(point4_rect3_shift*UP)
        )

        self.play(l.animate.shift(l_shift_horiz*LEFT))
        self.play(l.animate.rotate(3*PI/2))

        #poly_4 rand_points on perimeter
        point1_rect4 = Dot(color=dot_color, point=point1_rect3.get_center(), radius=dot_radius) #new top edge point
        point2_rect4 = Dot(color=dot_color, point=point2_rect3.get_center(), radius=dot_radius) #new right edge point
        point3_rect4 = Dot(color=dot_color, point=point3.get_center(), radius=dot_radius)  #new bottom edge point
        point4_rect4 = Dot(color=dot_color, point=point4_rect3.get_center(), radius=dot_radius) #new left edge point
        
        self.play(Create(point1_rect4), Create(point2_rect4), Create(point3_rect4), Create(point4_rect4))
        #reflection shift
        point1_rect4_shift = 2*abs(point1_rect4.get_center()[0] - rect_3.get_corner(direction=DL)[0])
        point2_rect4_shift = 2*abs(point2_rect4.get_center()[0] - rect_3.get_corner(direction=UL)[0])
        point3_rect4_shift = 2*abs(point3_rect4.get_center()[0] - rect_3.get_corner(direction=UL)[0])
        self.play(
            point1_rect4.animate.shift(point1_rect4_shift*LEFT),
            point2_rect4.animate.shift(point2_rect4_shift*LEFT),
            point3_rect4.animate.shift(point3_rect4_shift*LEFT)
            
        )
        self.play(Uncreate(l))


                                                    #Time for the inner rectangle

        
        #inner_peri_rect1
        peri_1 = Polygon(
        np.array(point1.get_center()), 
        np.array(point2.get_center()), 
        np.array(point3.get_center()), 
        np.array(point4.get_center()))
        self.play(Create(peri_1))

        #self.play(l.animate.shift(4*RIGHT, 1*DOWN))

        #inner_peri_rect2
        peri_2 = Polygon(
        np.array(point1_rect2.get_center()), 
        np.array(point2.get_center()), 
        np.array(point3_rect2.get_center()), 
        np.array(point4_rect2.get_center()))
        #self.play(l.animate.shift(1*UP))
        #self.play(l.animate.rotate(PI/2))

        #inner_peri_rect3
        peri_3 = Polygon(
        np.array(point1_rect3.get_center()), 
        np.array(point2_rect3.get_center()), 
        np.array(point3.get_center()), 
        np.array(point4_rect3.get_center()))
        #self.play(l.animate.shift(4*LEFT))
        #self.play(l.animate.rotate(3*PI/2))


        #inner_peri_rect4
        peri_4 = Polygon(
        np.array(point1_rect4.get_center()), 
        np.array(point2_rect4.get_center()), 
        np.array(point3_rect4.get_center()), 
        np.array(point4_rect4.get_center()))
        self.play(Create(peri_2), Create(peri_3), Create(peri_4))

        self.wait(5)




        #SOLUTION LINE
        sol_line = DashedLine(start = point1_rect2, end = point1_rect4, color = RED)
        self.play(Create(sol_line))


        
        
        #SHIFT!!!

        #MIDPOINT CALCS
        rect1_ul_corner = rect.get_corner(direction=UL)
        rect1_ur_corner = rect.get_corner(direction=UR)
        midpoint_up_edge_rect1 = (rect1_ul_corner[0] + rect1_ur_corner[0])/2
        midpoint_up_edge_rect1_point = Dot(color=dot_color, point=[midpoint_up_edge_rect1, point3.get_center()[1], 0], radius=dot_radius)
        #self.play(Create(midpoint_up_edge_rect1_point))


        rect2_dl_corner = rect_2.get_corner(direction=DL)
        rect2_dr_corner = rect_2.get_corner(direction=DR)
        midpoint_bottom_edge_rect2 = (rect2_dl_corner[0] + rect2_dr_corner[0])/2
        midpoint_bottom_edge_rect2_point = Dot(color=dot_color, point=[midpoint_bottom_edge_rect2, point1_rect2.get_center()[1], 0], radius=dot_radius)
        #self.play(Create(midpoint_bottom_edge_rect2_point))

        rect3_ul_corner = rect_3.get_corner(direction=UL)
        rect3_dl_corner = rect_3.get_corner(direction=DL)
        midpoint_left_edge_rect3 = (rect3_ul_corner[1] + rect3_dl_corner[1])/2
        midpoint_left_edge_rect3_point = Dot(color=dot_color, point=[point4_rect3.get_center()[0], midpoint_left_edge_rect3, 0], radius=dot_radius)
        #self.play(Create(midpoint_left_edge_rect3_point))

        rect4_ul_corner = rect_4.get_corner(direction=UL)
        rect4_ur_corner = rect_4.get_corner(direction=UR)
        midpoint_up_edge_rect4 = (rect4_ul_corner[0] + rect4_ur_corner[0])/2
        midpoint_up_edge_rect4_point = Dot(color=dot_color, point=[midpoint_up_edge_rect4, point1_rect4.get_center()[1], 0], radius=dot_radius)
        #self.play(Create(midpoint_up_edge_rect4_point))


#THE SHIFTS ARE NOT PROPERLY FUNCTIONAL
        #SHIFT IN RECT1: POINT3
        if (point3.get_center()[0] < midpoint_up_edge_rect1):
            shift_rect1 = point3.animate.shift((vec3[0])*RIGHT)

            peri_1_new = Polygon(
            np.array(point1.get_center()), 
            np.array(point2.get_center()), 
            np.array(point3.get_center() + [vec3[0], 0, 0]), 
            np.array(point4.get_center()))
            
            self.play(shift_rect1, Transform(peri_1, peri_1_new))

            #self.play(point3.animate.shift((vec3[0])*RIGHT))
        else:
            shift_rect1 = point3.animate.shift((vec3[0])*LEFT)
            
            peri_1_new = Polygon(
            np.array(point1.get_center()), 
            np.array(point2.get_center()), 
            np.array(point3.get_center() - [vec3[0], 0, 0]), 
            np.array(point4.get_center()))
            
            self.play(shift_rect1, Transform(peri_1, peri_1_new))
            
            # self.play(point3.animate.shift((vec3[0])*LEFT))

        #SHIFT IN RECT2: POINT1
        if (point1_rect2.get_center()[0] < midpoint_bottom_edge_rect2):
            shift_rect2 = point1_rect2.animate.shift((vec1[0])*RIGHT)

            peri_2_new = Polygon(
            np.array(point1_rect2.get_center() + [vec1[0], 0, 0]), 
            np.array(point2.get_center()), 
            np.array(point3_rect2.get_center()), 
            np.array(point4_rect2.get_center()))         
            
            self.play(shift_rect2, Transform(peri_2, peri_2_new))
        else:
            shift_rect2 = point1_rect2.animate.shift((vec1[0])*LEFT)

            peri_2_new = Polygon(
            np.array(point1_rect2.get_center() - [vec1[0], 0, 0]), 
            np.array(point2.get_center()), 
            np.array(point3_rect2.get_center()), 
            np.array(point4_rect2.get_center()))         
            
            self.play(shift_rect2, Transform(peri_2, peri_2_new))

        #SHIFT IN RECT3: POINT4
        if (point4_rect3.get_center()[0] < midpoint_left_edge_rect3):
            shift_rect3 = point4_rect3.animate.shift((vec4[0]*0.6)*UP)

            peri_3_new = Polygon(
            np.array(point1_rect3.get_center()), 
            np.array(point2_rect3.get_center()), 
            np.array(point3.get_center()), 
            np.array(point4_rect3.get_center() + [0, vec4[0]*0.6, 0]))

            self.play(shift_rect3, Transform(peri_3, peri_3_new))
        else:
            shift_rect3 = point4_rect3.animate.shift((vec4[0]*0.6)*DOWN)

            peri_3_new = Polygon(
            np.array(point1_rect3.get_center()), 
            np.array(point2_rect3.get_center()), 
            np.array(point3.get_center()), 
            np.array(point4_rect3.get_center() - [0, vec4[0]*0.6, 0]))

            self.play(shift_rect3, Transform(peri_3, peri_3_new))
        
        #SHIFT IN RECT4: POINT1
        if (point1_rect4.get_center()[0] < midpoint_up_edge_rect4):
            shift_rect4 = point1_rect4.animate.shift((vec1[0])*RIGHT)

            peri_4_new = Polygon(
            np.array(point1_rect4.get_center() + [vec1[0], 0, 0]), 
            np.array(point2_rect4.get_center()), 
            np.array(point3_rect4.get_center()), 
            np.array(point4_rect4.get_center()))

            self.play(shift_rect4, Transform(peri_4, peri_4_new))
        else:
            shift_rect4 = point1_rect4.animate.shift((vec1[0])*LEFT)

            peri_4_new = Polygon(
            np.array(point1_rect4.get_center() - [vec1[0], 0, 0]), 
            np.array(point2_rect4.get_center()), 
            np.array(point3_rect4.get_center()), 
            np.array(point4_rect4.get_center()))

            self.play(shift_rect4, Transform(peri_4, peri_4_new))

        

        #print(point3.get_center()[0])
        #self.remove(point2)
        # self.remove(point1, run_time = 4)
        # self.remove(point1_rect3, run_time = 4)
        # self.remove(point1_rect2, run_time = 4)
        self.wait(4)




class Daksh(Scene):
    def construct(self):
        sq = Rectangle()
        self.play(Create(sq))

        sq_dr_corner = sq.get_corner(direction=DR)
        sq_dl_corner = sq.get_corner(direction=DL)
        sq_ul_corner = sq.get_corner(direction=UL)
        sq_ur_corner = sq.get_corner(direction=UR)

        dot_radius = 0.1
        dot_color = color.PINK

        self.wait(1)

        vec1 = [-0.5, sq_dl_corner[1], 0]
        vec2 = [sq_ur_corner[0], 0.1, 0]
        vec3 = [0.8, sq_ul_corner[1], 0]
        vec4 = [sq_ul_corner[0], -0.3, 0]
        
        # vec1 = [(sq_dl_corner[0] + sq_dr_corner[0])/2, sq_dl_corner[1], 0] #bottom edge point
        # vec2 = [sq_ur_corner[0], (sq_dr_corner[1] + sq_ur_corner[1]-0.2)/2, 0] #right edge point
        # vec3 = [(sq_ul_corner[0] + sq_ur_corner[0])/2, sq_ul_corner[1], 0] #top edge point
        # vec4 = [sq_ul_corner[0], (sq_dr_corner[1] + sq_ur_corner[1])/2, 0] #left edge point
        
        #rect rand_points on perimeter
        point1 = Dot(color=dot_color, point=vec1, radius=dot_radius) #bottom edge point
        point2 = Dot(color=dot_color, point=vec2, radius=dot_radius) #right edge point
        point3 = Dot(color=dot_color, point=vec3, radius=dot_radius) #top edge point
        point4 = Dot(color=dot_color, point=vec4, radius=dot_radius) #left edge point
        self.play(Create(point1), Create(point2), Create(point3), Create(point4))

        #inner_peri_sq
        peri_1 = Polygon(
        np.array(point1.get_center()), 
        np.array(point2.get_center()), 
        np.array(point3.get_center()), 
        np.array(point4.get_center()))
        self.play(Create(peri_1))

        # s1 = point1.animate.shift(2*LEFT)
        # print(sq.get_vertices())
        # peri_1_new = Polygon(
        # np.array(point1.get_center() + [-2, 0, 0]), 
        # np.array(point2.get_center()), 
        # np.array(point3.get_center()), 
        # np.array(point4.get_center()))
        # self.play(s1, Transform(peri_1, peri_1_new))


class Euler(Scene):
    def construct(self):    
        cos_tay = Tex(r"$\cos(x) = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \frac{x^8}{8!}...$")
        cos_tay.scale(0.9)
        sin_tay = Tex(r"$\sin(x) = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \frac{x^9}{9!}...$")
        sin_tay.scale(0.9)
        e_tay = Tex(r"$e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!}...$")
        ei_tay = Tex(r"$e^{ix} = 1 + ix + \frac{(ix)^2}{2!} + \frac{(ix)^3}{3!} + \frac{(ix)^4}{4!}...$")
        ei_tay_simp = Tex(r"\ \\$= 1 + ix - \frac{x^2}{2!} - \frac{ix^3}{3!} + \frac{x^4}{4!} + \frac{ix^5}{5!}...$")
        cos_isin = Tex(r"$= \cos(x) + i\sin(x)$")
        e_cos_sin = Tex(r"$e^{ix} = \cos(x) + i\sin(x)$")
        x_pi = Tex(r"$\text{if } x = \pi$")
        e_cos_sin_pi = Tex(r"$e^{i\pi} = \cos(\pi) + i\sin(\pi)$")
        result = Tex(r"$e^{i\pi} = -1$")
        euler_id = Tex(r"$e^{i\pi} + 1 = 0$")
        runtime = 0.8
        self.play(Write(cos_tay), run_time = runtime)
        self.play(cos_tay.animate.shift(3.5*LEFT, 2*UP), run_time = runtime)
        self.play(Write(sin_tay), run_time = runtime)
        self.play(sin_tay.animate.shift(3.5*RIGHT, 2*UP), run_time = runtime)
        self.play(Write(e_tay), run_time = runtime)
        t1 = ReplacementTransform(e_tay, ei_tay)
        t2 = ei_tay_simp.shift(2*DOWN)
        t3 = ReplacementTransform(ei_tay_simp, cos_isin)
        t4 = ReplacementTransform(cos_isin, e_cos_sin)
        t5 = ReplacementTransform(e_cos_sin, e_cos_sin_pi)
        t6 = ReplacementTransform(e_cos_sin_pi, result)
        self.play(t1, run_time = runtime)
        self.wait
        self.play(Write(t2), run_time = runtime)
        self.play(Unwrite(ei_tay), run_time = runtime)
        self.play(t3, run_time = runtime)
        self.wait
        self.play(t4, run_time = runtime)
        self.play(Write(x_pi.shift(2*DOWN)), run_time = runtime)
        self.wait
        self.play(Unwrite(x_pi), t5, run_time = runtime)
        self.wait
        self.play(t6, run_time = runtime)
        self.play(ShrinkToCenter(sin_tay), ShrinkToCenter(cos_tay), Unwrite(result), run_time = runtime)
        self.play(Write(euler_id), run_time = runtime)
        

class magic_1(Scene):
    def construct(self):
        group = ellipse_1 = Ellipse(width=3, height=5, color=BLUE_B)
        a = Tex(r"a")
        b = Tex(r"b")
        c = Tex(r"a+b").scale(0.8)
        arrow_a = Arrow(start=np.array([0,0,0]), end=np.array([0.2, -0.8,0])).scale(2.2)
        arrow_b = Arrow(start=np.array([0,0,0]), end=np.array([0.5, -0.5,0])).scale(3)
        self.play(Create(group.shift(4*LEFT)), Create(a.shift(3.8*LEFT, 2*UP)), Create(b.shift(4.5*LEFT, 1.7*UP)))
        self.play(Create(arrow_a.shift(3.8*LEFT, 1.85*UP)), Create(arrow_b.shift(4.3*LEFT, 1.5*UP)))
        self.play(Write(c.shift(3.6*LEFT, 0.85*UP)))
        inverse = Tex(r"$a^{-1}$").scale(0.8)
        self.play(Write(inverse.shift(4.5*LEFT, 1*DOWN)))
        identity = Tex(r"$e$").scale(0.9)
        self.play(Write(identity.shift(3.3*LEFT, 1.2*DOWN)))
        self.wait(1)

        self.play(Write(Tex(r"GCD")))
        modn = Tex(r"$\mathbb{Z}_n$\\$\equiv mod(n)$").shift(4*RIGHT)
        self.wait(1)

        self.play(Write(modn))

class rotate(Scene):
    def construct(self):
        dot_color = WHITE
        point1 = Circle(radius=0.05)
        self.add(point1)
        # self.play(Rotate(point1, radians=PI/2))
        square=Square().scale(2)
        self.add(square)

        l = DashedLine(start = [3, -4, 0], end = [4, 4, 0])
        self.add(l)
        self.play(Create(point1))

        self.play(
            Rotate(
                square,
                PI/4,
                run_time=2
            )
        )
        self.wait(0.3)
        diff = l.get_start()
        self.play(Transform(point1, axis=l.get_center(), radians = PI))
        self.wait(0.3)


class fagnano_hard_code_positions(Scene):
    def construct(self):
        #First Rectangle
        rect = Rectangle()
        self.play(Create(rect))
        self.play(rect.animate.shift(2*DOWN, 0.5*RIGHT), run_time = 1.4)
        self.wait
        
        rect1_dr_corner = rect.get_corner(direction=DR)
        rect1_dl_corner = rect.get_corner(direction=DL)
        rect1_ul_corner = rect.get_corner(direction=UL)
        rect1_ur_corner = rect.get_corner(direction=UR)
        
        #Line of reflection
        reflection_line_start = [rect1_dr_corner[0], rect1_dr_corner[1]-1.5, 0]
        reflection_line_end = [rect1_dr_corner[0], rect1_ur_corner[1]+1.5, 0]
        l = DashedLine(start = reflection_line_start, 
                        end = reflection_line_end,
                        color = color.RED)
        self.play(Create(l, run_time = 1.6))
        
        #Second Rectangle
        rect_2 = Rectangle().shift(2*DOWN, 0.5*RIGHT)
        self.play(Create(rect_2))
        #second rect shift
        rect_2_shift = abs(rect1_dl_corner[0] - rect1_dr_corner[0])
        self.play(rect_2.animate.shift(rect_2_shift*RIGHT))
        
        #line of reflection vertcial shift
        l_shift_vert = 0.5*abs(rect1_ur_corner[1] - rect1_dr_corner[1])
        self.play(l.animate.shift(l_shift_vert*UP))
        self.play(l.animate.rotate(PI/2))
        
        #Third Rectangle
        rect_3 = Rectangle().shift(2*DOWN, 0.5*RIGHT)
        self.play(Create(rect_3))
        #third rect shift
        rect_3_shift = abs(rect1_dr_corner[1] - rect1_ur_corner[1])
        self.play(rect_3.animate.shift(rect_3_shift*UP))
        
        #line of reflection horizontal shift
        l_shift_horiz = abs(rect1_ur_corner[0] - rect1_ul_corner[0])
        self.play(l.animate.shift(l_shift_horiz*LEFT))
        self.play(l.animate.rotate(3*PI/2))

        #Fourth Rectangle
        rect_4 = Rectangle().shift(2*DOWN, 0.5*RIGHT)
        rect_4.shift(rect_3_shift*UP)
        self.play(Create(rect_4))
        #fourth rect shift
        self.play(rect_4.animate.shift(rect_2_shift*LEFT))
        
        #Random Points on the rectangle
        dot_radius = 0.1
        dot_color = color.PINK





        #MIDPOINT CALCS
        rect1_ul_corner = rect.get_corner(direction=UL)
        rect1_ur_corner = rect.get_corner(direction=UR)
        rect1_dl_corner = rect.get_corner(direction=DL)
        rect1_dr_corner = rect.get_corner(direction=DR)
        midpoint_top_edge_rect1 = (rect1_ul_corner[0] + rect1_ur_corner[0])/2
        midpoint_bottom_edge_rect1 = (rect1_dl_corner[0] + rect1_dr_corner[0])/2
        midpoint_left_edge_rect1 = (rect1_ul_corner[1] + rect1_dl_corner[1])/2
        midpoint_right_edge_rect1 = (rect1_ur_corner[1] + rect1_dr_corner[1])/2
        #midpoint_up_edge_rect1_point = Dot(color=dot_color, point=[midpoint_up_edge_rect1, point3.get_center()[1], 0], radius=dot_radius)
        #self.play(Create(midpoint_up_edge_rect1_point))


        rect2_dl_corner = rect_2.get_corner(direction=DL)
        rect2_dr_corner = rect_2.get_corner(direction=DR)
        rect2_ul_corner = rect_2.get_corner(direction=UL)
        rect2_ur_corner = rect_2.get_corner(direction=UR)
        midpoint_bottom_edge_rect2 = (rect2_dl_corner[0] + rect2_dr_corner[0])/2
        midpoint_top_edge_rect2 = (rect2_ul_corner[0] + rect2_ur_corner[0])/2
        midpoint_left_edge_rect2 = (rect2_ul_corner[1] + rect2_dl_corner[1])/2
        midpoint_right_edge_rect2 = (rect2_ur_corner[1] + rect2_dr_corner[1])/2
        #midpoint_bottom_edge_rect2_point = Dot(color=dot_color, point=[midpoint_bottom_edge_rect2, point1_rect2.get_center()[1], 0], radius=dot_radius)
        #self.play(Create(midpoint_bottom_edge_rect2_point))

        rect3_ul_corner = rect_3.get_corner(direction=UL)
        rect3_dl_corner = rect_3.get_corner(direction=DL)
        rect3_ur_corner = rect_3.get_corner(direction=UR)
        rect3_dr_corner = rect_3.get_corner(direction=DR)
        midpoint_left_edge_rect3 = (rect3_ul_corner[1] + rect3_dl_corner[1])/2
        midpoint_right_edge_rect3 = (rect3_ur_corner[1] + rect3_dr_corner[1])/2
        midpoint_top_edge_rect3 = (rect3_ul_corner[0] + rect3_ur_corner[0])/2
        midpoint_bottom_edge_rect3 = (rect3_dl_corner[0] + rect3_dr_corner[0])/2
        #midpoint_left_edge_rect3_point = Dot(color=dot_color, point=[point4_rect3.get_center()[0], midpoint_left_edge_rect3, 0], radius=dot_radius)
        #self.play(Create(midpoint_left_edge_rect3_point))

        rect4_ul_corner = rect_4.get_corner(direction=UL)
        rect4_ur_corner = rect_4.get_corner(direction=UR)
        rect4_dl_corner = rect_4.get_corner(direction=DL)
        rect4_dr_corner = rect_4.get_corner(direction=DR)
        midpoint_top_edge_rect4 = (rect4_ul_corner[0] + rect4_ur_corner[0])/2
        midpoint_bottom_edge_rect4 = (rect4_dl_corner[0] + rect4_dr_corner[0])/2
        midpoint_left_edge_rect4 = (rect4_ul_corner[1] + rect4_dl_corner[1])/2
        midpoint_right_edge_rect4 = (rect4_ur_corner[1] + rect4_dr_corner[1])/2
        #midpoint_up_edge_rect4_point = Dot(color=dot_color, point=[midpoint_up_edge_rect4, point1_rect4.get_center()[1], 0], radius=dot_radius)
        #self.play(Create(midpoint_up_edge_rect4_point))

        

        #HARD CODING POSITIONS

        vec1 = [midpoint_bottom_edge_rect1-1.5, rect1_dl_corner[1], 0] #bottom edge point
        vec2 = [rect1_ur_corner[0], midpoint_right_edge_rect1+0.3, 0] #right edge point
        vec3 = [midpoint_top_edge_rect1-0.7, rect1_ul_corner[1], 0] #top edge point
        vec4 = [rect1_ul_corner[0], midpoint_left_edge_rect1-0.3, 0] #left edge point
        
        #polygon rand_points on perimeter
        point1 = Dot(color=dot_color, point=vec1, radius=dot_radius) #bottom edge point
        point2 = Dot(color=dot_color, point=vec2, radius=dot_radius) #right edge point
        point3 = Dot(color=dot_color, point=vec3, radius=dot_radius) #top edge point
        point4 = Dot(color=dot_color, point=vec4, radius=dot_radius) #left edge point
        self.play(Create(point1), Create(point2), Create(point3), Create(point4))

        self.play(l.animate.shift(abs(rect1_dl_corner[0] - rect1_dr_corner[0])*RIGHT,
                                    0.5*abs(rect1_dr_corner[1] - rect1_ur_corner[1])*DOWN))
        
        
        #poly_2 rand_points on perimeter
        point1_rect2 = Dot(color=dot_color, point=vec1, radius=dot_radius) #bottom edge point on rect2
        #point2_rect2 = Dot(color=dot_color, point=vec2, radius=dot_radius) #left edge point on rect2
        point3_rect2 = Dot(color=dot_color, point=vec3, radius=dot_radius) #top edge point on rect2
        point4_rect2 = Dot(color=dot_color, point=vec4, radius=dot_radius) #right edge point on rect2
        self.play(Create(point1_rect2), Create(point3_rect2), Create(point4_rect2)) #, Create(point2_rect2)
        #reflection shift
        point1_rect2_shift = 2*abs(point1_rect2.get_center()[0] - rect1_dr_corner[0]) 
        point3_rect2_shift = 2*abs(point3_rect2.get_center()[0] - rect1_ur_corner[0]) 
        point4_rect2_shift = 2*abs(point4_rect2.get_center()[0] - rect1_ur_corner[0]) 
        self.play(
            point1_rect2.animate.shift(point1_rect2_shift*RIGHT),
            point3_rect2.animate.shift(point3_rect2_shift*RIGHT),
            point4_rect2.animate.shift(point4_rect2_shift*RIGHT)
        )
        
        self.play(l.animate.shift(l_shift_vert*UP))
        self.play(l.animate.rotate(PI/2))

        #poly_3 rand_points on perimeter
        point1_rect3 = Dot(color=dot_color, point=vec1, radius=dot_radius) #top edge point on rect3
        point2_rect3 = Dot(color=dot_color, point=vec2, radius=dot_radius) #right edge point on rect3
        #point3_rect3 = Dot(color=dot_color, point=vec3, radius=dot_radius) #bottom edge point on rect3
        point4_rect3 = Dot(color=dot_color, point=vec4, radius=dot_radius) #left edge point on rect3
       
        self.play(Create(point1_rect3), Create(point2_rect3), Create(point4_rect3)) #, Create(point3_rect3)
        #reflection shift
        point1_rect3_shift = 2*abs(point1_rect3.get_center()[1] - rect1_ur_corner[1]) 
        point2_rect3_shift = 2*abs(point2_rect3.get_center()[1] - rect1_ur_corner[1]) 
        point4_rect3_shift = 2*abs(point4_rect3.get_center()[1] - rect1_ul_corner[1]) 
        self.play(
            point1_rect3.animate.shift(point1_rect3_shift*UP),
            point2_rect3.animate.shift(point2_rect3_shift*UP),
            point4_rect3.animate.shift(point4_rect3_shift*UP)
        )

        self.play(l.animate.shift(l_shift_horiz*LEFT))
        self.play(l.animate.rotate(3*PI/2))

        #poly_4 rand_points on perimeter
        point1_rect4 = Dot(color=dot_color, point=point1_rect3.get_center(), radius=dot_radius) #new top edge point
        point2_rect4 = Dot(color=dot_color, point=point2_rect3.get_center(), radius=dot_radius) #new left edge point
        point3_rect4 = Dot(color=dot_color, point=point3.get_center(), radius=dot_radius)  #new bottom edge point
        #point4_rect4 = Dot(color=dot_color, point=point4_rect3.get_center(), radius=dot_radius) #new left edge point
        
        self.play(Create(point1_rect4), Create(point2_rect4), Create(point3_rect4))#, Create(point4_rect4))
        #reflection shift
        point1_rect4_shift = 2*abs(point1_rect4.get_center()[0] - rect_3.get_corner(direction=DL)[0])
        point2_rect4_shift = 2*abs(point2_rect4.get_center()[0] - rect_3.get_corner(direction=UL)[0])
        point3_rect4_shift = 2*abs(point3_rect4.get_center()[0] - rect_3.get_corner(direction=UL)[0])
        self.play(
            point1_rect4.animate.shift(point1_rect4_shift*LEFT),
            point2_rect4.animate.shift(point2_rect4_shift*LEFT),
            point3_rect4.animate.shift(point3_rect4_shift*LEFT)
            
        )
        self.play(Uncreate(l))


                                                    #Time for the inner rectangle

        
        #inner_peri_rect1
        peri_1 = Polygon(
        np.array(point1.get_center()), 
        np.array(point2.get_center()), 
        np.array(point3.get_center()), 
        np.array(point4.get_center()))
        self.play(Create(peri_1))

        #self.play(l.animate.shift(4*RIGHT, 1*DOWN))

        #inner_peri_rect2
        peri_2 = Polygon(
        np.array(point1_rect2.get_center()), 
        np.array(point2.get_center()), 
        np.array(point3_rect2.get_center()), 
        np.array(point4_rect2.get_center()))
        #self.play(l.animate.shift(1*UP))
        #self.play(l.animate.rotate(PI/2))

        #inner_peri_rect3
        peri_3 = Polygon(
        np.array(point1_rect3.get_center()), 
        np.array(point2_rect3.get_center()), 
        np.array(point3.get_center()), 
        np.array(point4_rect3.get_center()))
        #self.play(l.animate.shift(4*LEFT))
        #self.play(l.animate.rotate(3*PI/2))


        #inner_peri_rect4
        peri_4 = Polygon(
        np.array(point1_rect4.get_center()), 
        np.array(point2_rect4.get_center()), 
        np.array(point3_rect4.get_center()), 
        np.array(point4_rect3.get_center()))
        self.play(Create(peri_2), Create(peri_3), Create(peri_4))

    #    self.wait(3)




        #SOLUTION LINE
        sol_line = DashedLine(start = point1_rect2, end = point1_rect4, color = RED)
        self.play(Create(sol_line))



     #   self.wait(3)



        #SHIFT TIME (AGAIN HARD CODE)
        #SHIFTING POINT3
        n1 = 1
        shift1_rect1 = point3.animate.shift(n1*RIGHT)
        peri_1_new1 = Polygon(
        np.array(point1.get_center()), 
        np.array(point2.get_center()), 
        np.array(point3.get_center() + [n1, 0, 0]), 
        np.array(point4.get_center()))

        shift1_rect2 = point3_rect2.animate.shift(n1*LEFT)
        peri_2_new1 = Polygon(
        np.array(point1_rect2.get_center()), 
        np.array(point2.get_center()), 
        np.array(point3_rect2.get_center() - [n1, 0, 0]), 
        np.array(point4_rect2.get_center()))

        peri_3_new1 = Polygon(
        np.array(point1_rect3.get_center()), 
        np.array(point2_rect3.get_center()), 
        np.array(point3.get_center() + [n1, 0, 0]), 
        np.array(point4_rect3.get_center()))

        shift1_rect4 = point3_rect4.animate.shift(n1*RIGHT)
        peri_4_new1 = Polygon(
        np.array(point1_rect4.get_center()), 
        np.array(point2_rect4.get_center()), 
        np.array(point3_rect4.get_center() + [n1, 0, 0]), 
        np.array(point4_rect3.get_center()))

        
        self.play(shift1_rect1, shift1_rect2, shift1_rect4, 
        Transform(peri_1, peri_1_new1), Transform(peri_2, peri_2_new1), Transform(peri_3, peri_3_new1), Transform(peri_4, peri_4_new1))


     #   self.wait(1)


        #SHIFTING POINT1_RECT2
        n2 = 2
        shift2_rect2 = point1_rect2.animate.shift(n2*LEFT)
        peri_2_new2 = Polygon(
        np.array(point1_rect2.get_center() - [n2, 0, 0]), 
        np.array(point2.get_center()), 
        np.array(point3_rect2.get_center()), 
        np.array(point4_rect2.get_center()))

        shift2_rect1 = point1.animate.shift(n2*RIGHT)
        peri_1_new2 = Polygon(
        np.array(point1.get_center() + [n2, 0, 0]), 
        np.array(point2.get_center()), 
        np.array(point3.get_center()), 
        np.array(point4.get_center()))

        shift2_rect3 = point1_rect3.animate.shift(n2*RIGHT)
        peri_3_new2 = Polygon(
        np.array(point1_rect3.get_center() + [n2, 0, 0]), 
        np.array(point2_rect3.get_center()), 
        np.array(point3.get_center()), 
        np.array(point4_rect3.get_center()))

        shift2_rect4 = point1_rect4.animate.shift(n2*LEFT)
        peri_4_new2 = Polygon(
        np.array(point1_rect4.get_center() - [n2, 0, 0]), 
        np.array(point2_rect4.get_center()), 
        np.array(point3_rect4.get_center()), 
        np.array(point4_rect3.get_center()))

        sol_line_new1 = DashedLine(start = point1_rect2.get_center() - [n2, 0, 0], end = point1_rect4.get_center() - [n2, 0, 0], color = RED)

        self.play(shift2_rect1, shift2_rect2, shift2_rect4, shift2_rect3,
        Transform(peri_1, peri_1_new2), Transform(peri_2, peri_2_new2), Transform(peri_3, peri_3_new2), Transform(peri_4, peri_4_new2),
        Transform(sol_line, sol_line_new1))

        
    #    self.wait(1)


        #SHIFTING POINT4_RECT3
        n3 = 0.5
        shift3_rect3 = point4_rect3.animate.shift(n3*DOWN)
        peri_3_new3 = Polygon(
        np.array(point1_rect3.get_center()), 
        np.array(point2_rect3.get_center()), 
        np.array(point3.get_center()), 
        np.array(point4_rect3.get_center()) - [0, n3, 0])

        shift3_rect1 = point4.animate.shift(n3*UP)
        peri_1_new3 = Polygon(
        np.array(point1.get_center()), 
        np.array(point2.get_center()), 
        np.array(point3.get_center()), 
        np.array(point4.get_center() + [0, n3, 0]))

        shift3_rect2 = point4_rect2.animate.shift(n3*UP)
        peri_2_new3 = Polygon(
        np.array(point1_rect2.get_center()), 
        np.array(point2.get_center()), 
        np.array(point3_rect2.get_center()), 
        np.array(point4_rect2.get_center() + [0, n3, 0]))

        shift3_rect4 = point4_rect3.animate.shift(n3*DOWN)
        peri_4_new3 = Polygon(
        np.array(point1_rect4.get_center()), 
        np.array(point2_rect4.get_center()), 
        np.array(point3_rect4.get_center()), 
        np.array(point4_rect3.get_center() - [0, n3, 0]))
        
        self.play(shift3_rect1, shift3_rect2, shift3_rect3, shift3_rect4,
        Transform(peri_1, peri_1_new3), Transform(peri_2, peri_2_new3), Transform(peri_3, peri_3_new3), Transform(peri_4, peri_4_new3))



        #SHIFTING POINT2_RECT4
        n4 = 0.5
        shift4_rect4 = point2_rect4.animate.shift(n4*UP)
        peri_4_new4 = Polygon(
        np.array(point1_rect4.get_center()), 
        np.array(point2_rect4.get_center() + [0, n4, 0]), 
        np.array(point3_rect4.get_center()), 
        np.array(point4_rect3.get_center()))

        shift4_rect1 = point2.animate.shift(n4*DOWN)
        peri_1_new4 = Polygon(
        np.array(point1.get_center()), 
        np.array(point2.get_center() - [0, n4, 0]), 
        np.array(point3.get_center()), 
        np.array(point4.get_center()))

        peri_2_new4 = Polygon(
        np.array(point1_rect2.get_center()), 
        np.array(point2.get_center() - [0, n4, 0]), 
        np.array(point3_rect2.get_center()), 
        np.array(point4_rect2.get_center()))

        shift4_rect3 = point2_rect3.animate.shift(n4*UP)
        peri_3_new4 = Polygon(
        np.array(point1_rect3.get_center()), 
        np.array(point2_rect3.get_center() + [0, n4, 0]), 
        np.array(point3.get_center()), 
        np.array(point4_rect3.get_center()))

        self.play(shift4_rect1, shift4_rect3, shift4_rect4,
        Transform(peri_1, peri_1_new4), Transform(peri_2, peri_2_new4), Transform(peri_3, peri_3_new4), Transform(peri_4, peri_4_new4))


        #TIME FOR A SOLUTION

        #MIDPOINT SOLUTION

        #SHIFT POINT3_RECT1
        shift5_rect1 = point3.animate.move_to([midpoint_top_edge_rect1, point3.get_center()[1], 0])
        peri_1_new1 = Polygon(
        np.array(point1.get_center()), 
        np.array(point2.get_center()), 
        np.array([midpoint_top_edge_rect1, point3.get_center()[1], 0]), 
        np.array(point4.get_center()))

        shift5_rect2 = point3_rect2.animate.move_to([midpoint_top_edge_rect2, point3_rect2.get_center()[1], 0])
        peri_2_new1 = Polygon(
        np.array(point1_rect2.get_center()), 
        np.array(point2.get_center()), 
        np.array([midpoint_top_edge_rect2, point3_rect2.get_center()[1], 0]), 
        np.array(point4_rect2.get_center()))

        peri_3_new1 = Polygon(
        np.array(point1_rect3.get_center()), 
        np.array(point2_rect3.get_center()), 
        np.array([midpoint_top_edge_rect3, point3.get_center()[1], 0]), 
        np.array(point4_rect3.get_center()))

        shift5_rect4 = point3_rect4.animate.move_to([midpoint_top_edge_rect4, point3_rect4.get_center()[1], 0])
        peri_4_new1 = Polygon(
        np.array(point1_rect4.get_center()), 
        np.array(point2_rect4.get_center()), 
        np.array([midpoint_top_edge_rect4, point3_rect4.get_center()[1], 0]), 
        np.array(point4_rect3.get_center()))

        
        self.play(shift5_rect1, shift5_rect2, shift5_rect4, 
        Transform(peri_1, peri_1_new1), Transform(peri_2, peri_2_new1), Transform(peri_3, peri_3_new1), Transform(peri_4, peri_4_new1))

    #    self.wait(1)


        #SHIFTING POINT1_RECT2
        shift6_rect2 = point1_rect2.animate.move_to([midpoint_bottom_edge_rect2, point1_rect2.get_center()[1], 0])
        peri_2_new2 = Polygon(
        np.array([midpoint_bottom_edge_rect2, point1_rect2.get_center()[1], 0]), 
        np.array(point2.get_center()), 
        np.array(point3_rect2.get_center()), 
        np.array(point4_rect2.get_center()))

        shift6_rect1 = point1.animate.move_to([midpoint_bottom_edge_rect1, point1.get_center()[1], 0])
        peri_1_new2 = Polygon(
        np.array([midpoint_bottom_edge_rect1, point1.get_center()[1], 0]), 
        np.array(point2.get_center()), 
        np.array(point3.get_center()), 
        np.array(point4.get_center()))

        shift6_rect3 = point1_rect3.animate.move_to([midpoint_top_edge_rect3, point1_rect3.get_center()[1], 0])
        peri_3_new2 = Polygon(
        np.array([midpoint_top_edge_rect3, point1_rect3.get_center()[1], 0]), 
        np.array(point2_rect3.get_center()), 
        np.array(point3.get_center()), 
        np.array(point4_rect3.get_center()))

        shift6_rect4 = point1_rect4.animate.move_to([midpoint_top_edge_rect4, point1_rect4.get_center()[1], 0])
        peri_4_new2 = Polygon(
        np.array([midpoint_top_edge_rect4, point1_rect4.get_center()[1], 0]), 
        np.array(point2_rect4.get_center()), 
        np.array(point3_rect4.get_center()), 
        np.array(point4_rect3.get_center()))

        sol_line_new1 = DashedLine(start = [midpoint_bottom_edge_rect2, point1_rect2.get_center()[1], 0], end = [midpoint_top_edge_rect4, point1_rect4.get_center()[1], 0], color = RED)

        self.play(shift6_rect1, shift6_rect2, shift6_rect4, shift6_rect3,
        Transform(peri_1, peri_1_new2), Transform(peri_2, peri_2_new2), Transform(peri_3, peri_3_new2), Transform(peri_4, peri_4_new2),
        Transform(sol_line, sol_line_new1))

     #   self.wait(1)


        #SHIFTING POINT4_RECT3
        shift7_rect3 = point4_rect3.animate.move_to([point4_rect3.get_center()[0], midpoint_left_edge_rect3, 0])
        peri_3_new3 = Polygon(
        np.array(point1_rect3.get_center()), 
        np.array(point2_rect3.get_center()), 
        np.array(point3.get_center()), 
        np.array([point4_rect3.get_center()[0], midpoint_left_edge_rect3, 0]))

        shift7_rect1 = point4.animate.move_to([point4.get_center()[0], midpoint_left_edge_rect1, 0])
        peri_1_new3 = Polygon(
        np.array(point1.get_center()), 
        np.array(point2.get_center()), 
        np.array(point3.get_center()), 
        np.array([point4.get_center()[0], midpoint_left_edge_rect1, 0]))

        shift7_rect2 = point4_rect2.animate.move_to([point4_rect2.get_center()[0], midpoint_right_edge_rect2, 0])
        peri_2_new3 = Polygon(
        np.array(point1_rect2.get_center()), 
        np.array(point2.get_center()), 
        np.array(point3_rect2.get_center()), 
        np.array([point4_rect2.get_center()[0], midpoint_right_edge_rect2, 0]))

        #shift7_rect4 = point4_rect4.animate.move_to([point4_rect3.get_center()[0], midpoint_right_edge_rect3, 0])
        peri_4_new3 = Polygon(
        np.array(point1_rect4.get_center()), 
        np.array(point2_rect4.get_center()), 
        np.array(point3_rect4.get_center()), 
        np.array([point4_rect3.get_center()[0], midpoint_right_edge_rect3, 0]))
        
        self.play(shift7_rect3, shift7_rect2, shift7_rect1,
        Transform(peri_1, peri_1_new3), Transform(peri_2, peri_2_new3), Transform(peri_3, peri_3_new3), Transform(peri_4, peri_4_new3))

    #    self.wait(1)

        #SHIFTING POINT2_RECT4
        shift8_rect4 = point2_rect4.animate.move_to([point2_rect4.get_center()[0], midpoint_left_edge_rect4, 0])
        peri_4_new4 = Polygon(
        np.array(point1_rect4.get_center()), 
        np.array([point2_rect4.get_center()[0], midpoint_left_edge_rect4, 0]), 
        np.array(point3_rect4.get_center()), 
        np.array(point4_rect3.get_center()))

        shift8_rect1 = point2.animate.move_to([point2.get_center()[0], midpoint_right_edge_rect1, 0])
        peri_1_new4 = Polygon(
        np.array(point1.get_center()), 
        np.array([point2.get_center()[0], midpoint_right_edge_rect1, 0]), 
        np.array(point3.get_center()), 
        np.array(point4.get_center()))

        peri_2_new4 = Polygon(
        np.array(point1_rect2.get_center()), 
        np.array([point2.get_center()[0], midpoint_left_edge_rect2, 0]), 
        np.array(point3_rect2.get_center()), 
        np.array(point4_rect2.get_center()))

        shift8_rect3 = point2_rect3.animate.move_to([point2_rect3.get_center()[0], midpoint_right_edge_rect3, 0])
        peri_3_new4 = Polygon(
        np.array(point1_rect3.get_center()), 
        np.array([point2_rect3.get_center()[0], midpoint_right_edge_rect3, 0]), 
        np.array(point3.get_center()), 
        np.array(point4_rect3.get_center()))

        self.play(shift8_rect1, shift8_rect3, shift8_rect4,
        Transform(peri_1, peri_1_new4), Transform(peri_2, peri_2_new4), Transform(peri_3, peri_3_new4), Transform(peri_4, peri_4_new4))

        #NEAR_CORNER SOLUTION

        #SHIFT POINT3_RECT1
        n = 1.5
        s = -0.7

        shift9_rect1 = point3.animate.move_to([midpoint_top_edge_rect1+n, point3.get_center()[1], 0])
        peri_1_new_cor1 = Polygon(
        np.array([midpoint_bottom_edge_rect1-n, point1.get_center()[1], 0]), 
        np.array([point2.get_center()[0], midpoint_right_edge_rect1-s, 0]), 
        np.array([midpoint_top_edge_rect1+n, point3.get_center()[1], 0]), 
        np.array([point4.get_center()[0], midpoint_left_edge_rect1+s, 0]))

        shift9_rect2 = point3_rect2.animate.move_to([midpoint_top_edge_rect2-n, point3_rect2.get_center()[1], 0])
        peri_2_new_cor1 = Polygon(
        np.array([midpoint_bottom_edge_rect2+n, point1_rect2.get_center()[1], 0]), 
        np.array([point2.get_center()[0], midpoint_right_edge_rect1-s, 0]), 
        np.array([midpoint_top_edge_rect2-n, point3_rect2.get_center()[1], 0]), 
        np.array([point4_rect2.get_center()[0], midpoint_right_edge_rect2+s, 0]))

        peri_3_new_cor1 = Polygon(
        np.array([midpoint_top_edge_rect3-n, point1_rect3.get_center()[1], 0]), 
        np.array([point2_rect3.get_center()[0], midpoint_right_edge_rect3+s, 0]), 
        np.array([midpoint_top_edge_rect3+n, point3.get_center()[1], 0]), 
        np.array([point4_rect3.get_center()[0], midpoint_left_edge_rect3-s, 0]))

        shift9_rect4 = point3_rect4.animate.move_to([midpoint_top_edge_rect4-n, point3_rect4.get_center()[1], 0])
        peri_4_new_cor1 = Polygon(
        np.array([midpoint_top_edge_rect4+n, point1_rect4.get_center()[1], 0]), 
        np.array([point2_rect4.get_center()[0], midpoint_left_edge_rect4+s, 0]), 
        np.array([midpoint_top_edge_rect4-n, point3_rect4.get_center()[1], 0]), 
        np.array([point4_rect3.get_center()[0], midpoint_right_edge_rect3-s, 0]))

        shift10_rect2 = point1_rect2.animate.move_to([midpoint_bottom_edge_rect2+n, point1_rect2.get_center()[1], 0])
        shift10_rect1 = point1.animate.move_to([midpoint_bottom_edge_rect1-n, point1.get_center()[1], 0])
        shift10_rect3 = point1_rect3.animate.move_to([midpoint_top_edge_rect3-n, point1_rect3.get_center()[1], 0])
        shift10_rect4 = point1_rect4.animate.move_to([midpoint_top_edge_rect4+n, point1_rect4.get_center()[1], 0])
        
        sol_line_new_cor1 = DashedLine(start = [midpoint_bottom_edge_rect2+n, point1_rect2.get_center()[1], 0], end = [midpoint_top_edge_rect4+n, point1_rect4.get_center()[1], 0], color = RED)

        shift11_rect3 = point4_rect3.animate.move_to([point4_rect3.get_center()[0], midpoint_left_edge_rect3-s, 0])
        shift11_rect1 = point4.animate.move_to([point4.get_center()[0], midpoint_left_edge_rect1+s, 0])
        shift11_rect2 = point4_rect2.animate.move_to([point4_rect2.get_center()[0], midpoint_right_edge_rect2+s, 0])
        
        shift12_rect4 = point2_rect4.animate.move_to([point2_rect4.get_center()[0], midpoint_left_edge_rect4+s, 0])
        shift12_rect1 = point2.animate.move_to([point2.get_center()[0], midpoint_right_edge_rect1-s, 0])
        shift12_rect3 = point2_rect3.animate.move_to([point2_rect3.get_center()[0], midpoint_right_edge_rect3+s, 0])
        
        self.play(shift9_rect1, shift9_rect2, shift9_rect4, 
        shift10_rect4, shift10_rect3, shift10_rect1, shift10_rect2,
        shift11_rect3, shift11_rect1, shift11_rect2,
        shift12_rect4, shift12_rect1, shift12_rect3,
        Transform(peri_1, peri_1_new_cor1), Transform(peri_2, peri_2_new_cor1), Transform(peri_3, peri_3_new_cor1), Transform(peri_4, peri_4_new_cor1),
        Transform(sol_line, sol_line_new_cor1))

        self.wait(1)


#         #SHIFTING POINT1_RECT2
#         shift10_rect2 = point1_rect2.animate.move_to([midpoint_bottom_edge_rect2+n, point1_rect2.get_center()[1], 0])
#         peri_2_new2 = Polygon(
#         np.array([midpoint_bottom_edge_rect2+n, point1_rect2.get_center()[1], 0]), 
#         np.array(point2.get_center()), 
#         np.array(point3_rect2.get_center()), 
#         np.array(point4_rect2.get_center()))

#         shift10_rect1 = point1.animate.move_to([midpoint_bottom_edge_rect1-n, point1.get_center()[1], 0])
#         peri_1_new2 = Polygon(
#         np.array([midpoint_bottom_edge_rect1-n, point1.get_center()[1], 0]), 
#         np.array(point2.get_center()), 
#         np.array(point3.get_center()), 
#         np.array(point4.get_center()))

#         shift10_rect3 = point1_rect3.animate.move_to([midpoint_top_edge_rect3-n, point1_rect3.get_center()[1], 0])
#         peri_3_new2 = Polygon(
#         np.array([midpoint_top_edge_rect3-n, point1_rect3.get_center()[1], 0]), 
#         np.array(point2_rect3.get_center()), 
#         np.array(point3.get_center()), 
#         np.array(point4_rect3.get_center()))

#         shift10_rect4 = point1_rect4.animate.move_to([midpoint_top_edge_rect4+n, point1_rect4.get_center()[1], 0])
#         peri_4_new2 = Polygon(
#         np.array([midpoint_top_edge_rect4+n, point1_rect4.get_center()[1], 0]), 
#         np.array(point2_rect4.get_center()), 
#         np.array(point3_rect4.get_center()), 
#         np.array(point4_rect3.get_center()))

#         sol_line_new_cor1 = DashedLine(start = [midpoint_bottom_edge_rect2+n, point1_rect2.get_center()[1], 0], end = [midpoint_top_edge_rect4+n, point1_rect4.get_center()[1], 0], color = RED)

#         self.play(shift10_rect1, shift10_rect2, shift10_rect4, shift10_rect3,
#         Transform(peri_1, peri_1_new2), Transform(peri_2, peri_2_new2), Transform(peri_3, peri_3_new2), Transform(peri_4, peri_4_new2),
#         Transform(sol_line, sol_line_new1))


# #        SHIFTING POINT4_RECT3
#         s = -0.7
#         shift11_rect3 = point4_rect3.animate.move_to([point4_rect3.get_center()[0], midpoint_left_edge_rect3-s, 0])
#         peri_3_new3 = Polygon(
#         np.array(point1_rect3.get_center()), 
#         np.array(point2_rect3.get_center()), 
#         np.array(point3.get_center()), 
#         np.array([point4_rect3.get_center()[0], midpoint_left_edge_rect3-s, 0]))

#         shift11_rect1 = point4.animate.move_to([point4.get_center()[0], midpoint_left_edge_rect1+s, 0])
#         peri_1_new3 = Polygon(
#         np.array(point1.get_center()), 
#         np.array(point2.get_center()), 
#         np.array(point3.get_center()), 
#         np.array([point4.get_center()[0], midpoint_left_edge_rect1+s, 0]))

#         shift11_rect2 = point4_rect2.animate.move_to([point4_rect2.get_center()[0], midpoint_right_edge_rect2+s, 0])
#         peri_2_new3 = Polygon(
#         np.array(point1_rect2.get_center()), 
#         np.array(point2.get_center()), 
#         np.array(point3_rect2.get_center()), 
#         np.array([point4_rect2.get_center()[0], midpoint_right_edge_rect2+s, 0]))

#         shift11_rect4 = point4_rect3.animate.move_to([point4_rect3.get_center()[0], midpoint_right_edge_rect3, 0])
#         peri_4_new3 = Polygon(
#         np.array(point1_rect4.get_center()), 
#         np.array(point2_rect4.get_center()), 
#         np.array(point3_rect4.get_center()), 
#         np.array([point4_rect3.get_center()[0], midpoint_right_edge_rect3-s, 0]))
        
#         self.play(shift11_rect3, shift11_rect2, shift11_rect1,
#         Transform(peri_1, peri_1_new3), Transform(peri_2, peri_2_new3), Transform(peri_3, peri_3_new3), Transform(peri_4, peri_4_new3))

#         self.wait(1)

#         #SHIFTING POINT2_RECT4
#         shift12_rect4 = point2_rect4.animate.move_to([point2_rect4.get_center()[0], midpoint_left_edge_rect4+s, 0])
#         peri_4_new4 = Polygon(
#         np.array(point1_rect4.get_center()), 
#         np.array([point2_rect4.get_center()[0], midpoint_left_edge_rect4+s, 0]), 
#         np.array(point3_rect4.get_center()), 
#         np.array(point4_rect3.get_center()))

#         shift12_rect1 = point2.animate.move_to([point2.get_center()[0], midpoint_right_edge_rect1-s, 0])
#         peri_1_new4 = Polygon(
#         np.array(point1.get_center()), 
#         np.array([point2.get_center()[0], midpoint_right_edge_rect1-s, 0]), 
#         np.array(point3.get_center()), 
#         np.array(point4.get_center()))

#         peri_2_new4 = Polygon(
#         np.array(point1_rect2.get_center()), 
#         np.array([point2.get_center()[0], midpoint_left_edge_rect2-s, 0]), 
#         np.array(point3_rect2.get_center()), 
#         np.array(point4_rect2.get_center()))

#         shift12_rect3 = point2_rect3.animate.move_to([point2_rect3.get_center()[0], midpoint_right_edge_rect3+s, 0])
#         peri_3_new4 = Polygon(
#         np.array(point1_rect3.get_center()), 
#         np.array([point2_rect3.get_center()[0], midpoint_right_edge_rect3+s, 0]), 
#         np.array(point3.get_center()), 
#         np.array(point4_rect3.get_center()))

#         self.play(shift12_rect1, shift12_rect3, shift12_rect4,
#         Transform(peri_1, peri_1_new4), Transform(peri_2, peri_2_new4), Transform(peri_3, peri_3_new4), Transform(peri_4, peri_4_new4))
        
        #ANOTHER NEAR_CORNER SOLUTION

        #SHIFT POINT3_RECT1
        n = -1.5
        s = 0.7

        shift9_rect1 = point3.animate.move_to([midpoint_top_edge_rect1+n, point3.get_center()[1], 0])
        peri_1_new_cor1 = Polygon(
        np.array([midpoint_bottom_edge_rect1-n, point1.get_center()[1], 0]), 
        np.array([point2.get_center()[0], midpoint_right_edge_rect1-s, 0]), 
        np.array([midpoint_top_edge_rect1+n, point3.get_center()[1], 0]), 
        np.array([point4.get_center()[0], midpoint_left_edge_rect1+s, 0]))

        shift9_rect2 = point3_rect2.animate.move_to([midpoint_top_edge_rect2-n, point3_rect2.get_center()[1], 0])
        peri_2_new_cor1 = Polygon(
        np.array([midpoint_bottom_edge_rect2+n, point1_rect2.get_center()[1], 0]), 
        np.array([point2.get_center()[0], midpoint_right_edge_rect1-s, 0]), 
        np.array([midpoint_top_edge_rect2-n, point3_rect2.get_center()[1], 0]), 
        np.array([point4_rect2.get_center()[0], midpoint_right_edge_rect2+s, 0]))

        peri_3_new_cor1 = Polygon(
        np.array([midpoint_top_edge_rect3-n, point1_rect3.get_center()[1], 0]), 
        np.array([point2_rect3.get_center()[0], midpoint_right_edge_rect3+s, 0]), 
        np.array([midpoint_top_edge_rect3+n, point3.get_center()[1], 0]), 
        np.array([point4_rect3.get_center()[0], midpoint_left_edge_rect3-s, 0]))

        shift9_rect4 = point3_rect4.animate.move_to([midpoint_top_edge_rect4-n, point3_rect4.get_center()[1], 0])
        peri_4_new_cor1 = Polygon(
        np.array([midpoint_top_edge_rect4+n, point1_rect4.get_center()[1], 0]), 
        np.array([point2_rect4.get_center()[0], midpoint_left_edge_rect4+s, 0]), 
        np.array([midpoint_top_edge_rect4-n, point3_rect4.get_center()[1], 0]), 
        np.array([point4_rect3.get_center()[0], midpoint_right_edge_rect3-s, 0]))

        shift10_rect2 = point1_rect2.animate.move_to([midpoint_bottom_edge_rect2+n, point1_rect2.get_center()[1], 0])
        shift10_rect1 = point1.animate.move_to([midpoint_bottom_edge_rect1-n, point1.get_center()[1], 0])
        shift10_rect3 = point1_rect3.animate.move_to([midpoint_top_edge_rect3-n, point1_rect3.get_center()[1], 0])
        shift10_rect4 = point1_rect4.animate.move_to([midpoint_top_edge_rect4+n, point1_rect4.get_center()[1], 0])
        
        sol_line_new_cor1 = DashedLine(start = [midpoint_bottom_edge_rect2+n, point1_rect2.get_center()[1], 0], end = [midpoint_top_edge_rect4+n, point1_rect4.get_center()[1], 0], color = RED)

        shift11_rect3 = point4_rect3.animate.move_to([point4_rect3.get_center()[0], midpoint_left_edge_rect3-s, 0])
        shift11_rect1 = point4.animate.move_to([point4.get_center()[0], midpoint_left_edge_rect1+s, 0])
        shift11_rect2 = point4_rect2.animate.move_to([point4_rect2.get_center()[0], midpoint_right_edge_rect2+s, 0])
        
        shift12_rect4 = point2_rect4.animate.move_to([point2_rect4.get_center()[0], midpoint_left_edge_rect4+s, 0])
        shift12_rect1 = point2.animate.move_to([point2.get_center()[0], midpoint_right_edge_rect1-s, 0])
        shift12_rect3 = point2_rect3.animate.move_to([point2_rect3.get_center()[0], midpoint_right_edge_rect3+s, 0])
        
        self.play(shift9_rect1, shift9_rect2, shift9_rect4, 
        shift10_rect4, shift10_rect3, shift10_rect1, shift10_rect2,
        shift11_rect3, shift11_rect1, shift11_rect2,
        shift12_rect4, shift12_rect1, shift12_rect3,
        Transform(peri_1, peri_1_new_cor1), Transform(peri_2, peri_2_new_cor1), Transform(peri_3, peri_3_new_cor1), Transform(peri_4, peri_4_new_cor1),
        Transform(sol_line, sol_line_new_cor1))

        self.wait(1)






        #ANOTHER SOLUTION

        #SHIFT POINT3_RECT1
        n = -1.5*(0.7)
        s = 0.7*(0.7)

        shift9_rect1 = point3.animate.move_to([midpoint_top_edge_rect1+n, point3.get_center()[1], 0])
        peri_1_new_cor1 = Polygon(
        np.array([midpoint_bottom_edge_rect1-n, point1.get_center()[1], 0]), 
        np.array([point2.get_center()[0], midpoint_right_edge_rect1-s, 0]), 
        np.array([midpoint_top_edge_rect1+n, point3.get_center()[1], 0]), 
        np.array([point4.get_center()[0], midpoint_left_edge_rect1+s, 0]))

        shift9_rect2 = point3_rect2.animate.move_to([midpoint_top_edge_rect2-n, point3_rect2.get_center()[1], 0])
        peri_2_new_cor1 = Polygon(
        np.array([midpoint_bottom_edge_rect2+n, point1_rect2.get_center()[1], 0]), 
        np.array([point2.get_center()[0], midpoint_right_edge_rect1-s, 0]), 
        np.array([midpoint_top_edge_rect2-n, point3_rect2.get_center()[1], 0]), 
        np.array([point4_rect2.get_center()[0], midpoint_right_edge_rect2+s, 0]))

        peri_3_new_cor1 = Polygon(
        np.array([midpoint_top_edge_rect3-n, point1_rect3.get_center()[1], 0]), 
        np.array([point2_rect3.get_center()[0], midpoint_right_edge_rect3+s, 0]), 
        np.array([midpoint_top_edge_rect3+n, point3.get_center()[1], 0]), 
        np.array([point4_rect3.get_center()[0], midpoint_left_edge_rect3-s, 0]))

        shift9_rect4 = point3_rect4.animate.move_to([midpoint_top_edge_rect4-n, point3_rect4.get_center()[1], 0])
        peri_4_new_cor1 = Polygon(
        np.array([midpoint_top_edge_rect4+n, point1_rect4.get_center()[1], 0]), 
        np.array([point2_rect4.get_center()[0], midpoint_left_edge_rect4+s, 0]), 
        np.array([midpoint_top_edge_rect4-n, point3_rect4.get_center()[1], 0]), 
        np.array([point4_rect3.get_center()[0], midpoint_right_edge_rect3-s, 0]))

        shift10_rect2 = point1_rect2.animate.move_to([midpoint_bottom_edge_rect2+n, point1_rect2.get_center()[1], 0])
        shift10_rect1 = point1.animate.move_to([midpoint_bottom_edge_rect1-n, point1.get_center()[1], 0])
        shift10_rect3 = point1_rect3.animate.move_to([midpoint_top_edge_rect3-n, point1_rect3.get_center()[1], 0])
        shift10_rect4 = point1_rect4.animate.move_to([midpoint_top_edge_rect4+n, point1_rect4.get_center()[1], 0])
        
        sol_line_new_cor1 = DashedLine(start = [midpoint_bottom_edge_rect2+n, point1_rect2.get_center()[1], 0], end = [midpoint_top_edge_rect4+n, point1_rect4.get_center()[1], 0], color = RED)

        shift11_rect3 = point4_rect3.animate.move_to([point4_rect3.get_center()[0], midpoint_left_edge_rect3-s, 0])
        shift11_rect1 = point4.animate.move_to([point4.get_center()[0], midpoint_left_edge_rect1+s, 0])
        shift11_rect2 = point4_rect2.animate.move_to([point4_rect2.get_center()[0], midpoint_right_edge_rect2+s, 0])
        
        shift12_rect4 = point2_rect4.animate.move_to([point2_rect4.get_center()[0], midpoint_left_edge_rect4+s, 0])
        shift12_rect1 = point2.animate.move_to([point2.get_center()[0], midpoint_right_edge_rect1-s, 0])
        shift12_rect3 = point2_rect3.animate.move_to([point2_rect3.get_center()[0], midpoint_right_edge_rect3+s, 0])
        
        self.play(shift9_rect1, shift9_rect2, shift9_rect4, 
        shift10_rect4, shift10_rect3, shift10_rect1, shift10_rect2,
        shift11_rect3, shift11_rect1, shift11_rect2,
        shift12_rect4, shift12_rect1, shift12_rect3,
        Transform(peri_1, peri_1_new_cor1), Transform(peri_2, peri_2_new_cor1), Transform(peri_3, peri_3_new_cor1), Transform(peri_4, peri_4_new_cor1),
        Transform(sol_line, sol_line_new_cor1))

        self.wait(1)







        #ANOTHER SOLUTION

        #SHIFT POINT3_RECT1
        n = 1.5*(0.7)
        s = -0.7*(0.7)

        shift9_rect1 = point3.animate.move_to([midpoint_top_edge_rect1+n, point3.get_center()[1], 0])
        peri_1_new_cor1 = Polygon(
        np.array([midpoint_bottom_edge_rect1-n, point1.get_center()[1], 0]), 
        np.array([point2.get_center()[0], midpoint_right_edge_rect1-s, 0]), 
        np.array([midpoint_top_edge_rect1+n, point3.get_center()[1], 0]), 
        np.array([point4.get_center()[0], midpoint_left_edge_rect1+s, 0]))

        shift9_rect2 = point3_rect2.animate.move_to([midpoint_top_edge_rect2-n, point3_rect2.get_center()[1], 0])
        peri_2_new_cor1 = Polygon(
        np.array([midpoint_bottom_edge_rect2+n, point1_rect2.get_center()[1], 0]), 
        np.array([point2.get_center()[0], midpoint_right_edge_rect1-s, 0]), 
        np.array([midpoint_top_edge_rect2-n, point3_rect2.get_center()[1], 0]), 
        np.array([point4_rect2.get_center()[0], midpoint_right_edge_rect2+s, 0]))

        peri_3_new_cor1 = Polygon(
        np.array([midpoint_top_edge_rect3-n, point1_rect3.get_center()[1], 0]), 
        np.array([point2_rect3.get_center()[0], midpoint_right_edge_rect3+s, 0]), 
        np.array([midpoint_top_edge_rect3+n, point3.get_center()[1], 0]), 
        np.array([point4_rect3.get_center()[0], midpoint_left_edge_rect3-s, 0]))

        shift9_rect4 = point3_rect4.animate.move_to([midpoint_top_edge_rect4-n, point3_rect4.get_center()[1], 0])
        peri_4_new_cor1 = Polygon(
        np.array([midpoint_top_edge_rect4+n, point1_rect4.get_center()[1], 0]), 
        np.array([point2_rect4.get_center()[0], midpoint_left_edge_rect4+s, 0]), 
        np.array([midpoint_top_edge_rect4-n, point3_rect4.get_center()[1], 0]), 
        np.array([point4_rect3.get_center()[0], midpoint_right_edge_rect3-s, 0]))

        shift10_rect2 = point1_rect2.animate.move_to([midpoint_bottom_edge_rect2+n, point1_rect2.get_center()[1], 0])
        shift10_rect1 = point1.animate.move_to([midpoint_bottom_edge_rect1-n, point1.get_center()[1], 0])
        shift10_rect3 = point1_rect3.animate.move_to([midpoint_top_edge_rect3-n, point1_rect3.get_center()[1], 0])
        shift10_rect4 = point1_rect4.animate.move_to([midpoint_top_edge_rect4+n, point1_rect4.get_center()[1], 0])
        
        sol_line_new_cor1 = DashedLine(start = [midpoint_bottom_edge_rect2+n, point1_rect2.get_center()[1], 0], end = [midpoint_top_edge_rect4+n, point1_rect4.get_center()[1], 0], color = RED)

        shift11_rect3 = point4_rect3.animate.move_to([point4_rect3.get_center()[0], midpoint_left_edge_rect3-s, 0])
        shift11_rect1 = point4.animate.move_to([point4.get_center()[0], midpoint_left_edge_rect1+s, 0])
        shift11_rect2 = point4_rect2.animate.move_to([point4_rect2.get_center()[0], midpoint_right_edge_rect2+s, 0])
        
        shift12_rect4 = point2_rect4.animate.move_to([point2_rect4.get_center()[0], midpoint_left_edge_rect4+s, 0])
        shift12_rect1 = point2.animate.move_to([point2.get_center()[0], midpoint_right_edge_rect1-s, 0])
        shift12_rect3 = point2_rect3.animate.move_to([point2_rect3.get_center()[0], midpoint_right_edge_rect3+s, 0])
        
        self.play(shift9_rect1, shift9_rect2, shift9_rect4, 
        shift10_rect4, shift10_rect3, shift10_rect1, shift10_rect2,
        shift11_rect3, shift11_rect1, shift11_rect2,
        shift12_rect4, shift12_rect1, shift12_rect3,
        Transform(peri_1, peri_1_new_cor1), Transform(peri_2, peri_2_new_cor1), Transform(peri_3, peri_3_new_cor1), Transform(peri_4, peri_4_new_cor1),
        Transform(sol_line, sol_line_new_cor1))

        self.wait(1)

        #Creation of diagonals
        self.play(Uncreate(sol_line))

        d1_rect1 = Line(start=rect1_dl_corner, end=rect1_ur_corner)
        d2_rect1 = Line(start=rect1_dr_corner, end=rect1_ul_corner)

        d1_rect2 = Line(start=rect2_dl_corner, end=rect2_ur_corner)
        d2_rect2 = Line(start=rect2_dr_corner, end=rect2_ul_corner)

        d1_rect3 = Line(start=rect3_dl_corner, end=rect3_ur_corner)
        d2_rect3 = Line(start=rect3_dr_corner, end=rect3_ul_corner)

        d1_rect4 = Line(start=rect4_dl_corner, end=rect4_ur_corner)
        d2_rect4 = Line(start=rect4_dr_corner, end=rect4_ul_corner)

        self.play(
            Create(d1_rect1), Create(d2_rect1),
            Create(d1_rect2), Create(d2_rect2),
            Create(d1_rect3), Create(d2_rect3),
            Create(d1_rect4), Create(d2_rect4),
        )

        self.wait(1)