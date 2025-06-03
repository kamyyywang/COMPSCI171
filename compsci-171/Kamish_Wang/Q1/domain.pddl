(define (domain cooking)
    (:requirements :typing)
    (:types 
        tile countertop pot ingredient cook
    )
    (:predicates
        (at ?c - cook ?t - tile)
        (adjacent ?t1 ?t2 - tile)
        (adjacent-counter ?t - tile ?ctr - countertop)
        (ingredient-on ?i - ingredient ?ctr - countertop)
        (pot-on ?p - pot ?ctr - countertop)
        (holding ?c - cook ?i - ingredient)
        (ingredient-in-pot ?i - ingredient ?p - pot)
    )
    (:action move
    :parameters (?c - cook ?from ?to - tile)
    :precondition (and (at ?c ?from) (adjacent ?from ?to))
    :effect (and (at ?c ?to) (not (at ?c ?from))))
    (:action pickup
    :parameters (?c - cook ?i - ingredient ?ctr - countertop ?t - tile)
    :precondition (and (at ?c ?t) (ingredient-on ?i ?ctr) (adjacent-counter ?t ?ctr))
    :effect (and (holding ?c ?i) (not (ingredient-on ?i ?ctr))))  
    (:action drop-into-pot
    :parameters (?c - cook ?i - ingredient ?p - pot ?ctr - countertop ?t - tile)
    :precondition (and (holding ?c ?i) (at ?c ?t) (pot-on ?p ?ctr) (adjacent-counter ?t ?ctr))
    :effect (and (ingredient-in-pot ?i ?p) (not (holding ?c ?i))))
)