(define (problem cook-dish)
  (:domain cooking)
    (:objects
        g1 g2 g3 g4 g5 g6 g7 - tile
        ctr1 ctr2 ctr3 ctr4 ctr5 - countertop
        pot1 - pot
        ingredient1 ingredient2 ingredient3 - ingredient
        cook1 cook2 - cook
    )
    (:init
        (at cook1 g1)
        (at cook2 g6)

        (pot-on pot1 ctr1)

        (ingredient-on ingredient1 ctr3)
        (ingredient-on ingredient2 ctr4)
        (ingredient-on ingredient3 ctr5)

        (adjacent g1 g2)
        (adjacent g2 g1)
        
        (adjacent g2 g5)
        (adjacent g5 g2)
        
        (adjacent g2 g3)
        (adjacent g3 g2)
        
        (adjacent g2 g4)
        (adjacent g4 g2)
        
        (adjacent g3 g1)
        (adjacent g1 g3)
        
        (adjacent g1 g4)
        (adjacent g4 g1)
        
        (adjacent g3 g6)
        (adjacent g6 g3)
        
        (adjacent g3 g4)
        (adjacent g4 g3)
        
        (adjacent g4 g6)
        (adjacent g6 g4)
        
        (adjacent g4 g7)
        (adjacent g7 g4)
        
        (adjacent g5 g7)
        (adjacent g7 g5)
        
        (adjacent g4 g5)
        (adjacent g5 g4)
        
        (adjacent g5 g6)
        (adjacent g6 g5)
        
        (adjacent g6 g7)
        (adjacent g7 g6)
        
        (adjacent-counter g2 ctr1)
        (adjacent-counter g5 ctr1)
        (adjacent-counter g4 ctr1)
        (adjacent-counter g2 ctr2)
        (adjacent-counter g5 ctr3)
        (adjacent-counter g7 ctr3)
        (adjacent-counter g4 ctr3)
        (adjacent-counter g3 ctr4)
        (adjacent-counter g4 ctr4)
        (adjacent-counter g6 ctr4)
        (adjacent-counter g5 ctr5)
        (adjacent-counter g7 ctr5)
    )
    (:goal (and
        (at cook1 g1)
        (at cook2 g6)
        (ingredient-in-pot ingredient1 pot1)
        (ingredient-in-pot ingredient2 pot1)
        (ingredient-in-pot ingredient3 pot1)
    ))
)