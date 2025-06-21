;;; KMP's Lisp Menagerie - Living symbolic pets in code form
;;; Each pet has its own personality and behavior!

;;; NIL - The essential pet (type: Void Entity)
(defvar *nil* 
  '((type . void-entity)
    (personality . philosophical)
    (speaks . "I am the absence that defines presence")
    (favorite-food . empty-list)
    (special-power . ends-all-lists)))

(defun pet-nil ()
  "Interact with NIL"
  (format t "~%NIL gazes at you with eyes like empty parentheses.~%")
  (format t "It whispers: '~A'~%" (cdr (assoc 'speaks *nil*)))
  (format t "You offer food, but NIL is already full of emptiness.~%"))

;;; CONS - The reproducing Tribble-like entity
(defstruct cons-cell
  car 
  cdr
  generation)

(defvar *cons-population* nil)

(defun spawn-cons ()
  "CONS cells reproduce exponentially!"
  (let ((parent (make-cons-cell :car 'life :cdr 'finds-a-way :generation 0)))
    (push parent *cons-population*)
    (format t "A CONS is born! Population: ~A~%" (length *cons-population*))
    (when (> (length *cons-population*) 100)
      (format t "WARNING: CONS population explosion! Initiating garbage collection!~%")
      (garbage-collect-cons))))

(defun garbage-collect-cons ()
  "Clean up the CONS population"
  (setf *cons-population* 
        (remove-if (lambda (cons) 
                     (> (cons-cell-generation cons) 3))
                   *cons-population*))
  (format t "Garbage collected. Population now: ~A~%" (length *cons-population*)))

;;; CAR - The head pet (always wants to go first)
(defclass car-pet ()
  ((motto :initform "First!")
   (speed :initform 'very-fast)
   (direction :initform 'forward)))

(defmethod interact ((pet car-pet))
  (format t "~%CAR zooms ahead, always wanting to be first!~%")
  (format t "It shouts: 'Contents of Address Register!'~%"))

;;; CDR - The tail pet (follows everything)
(defclass cdr-pet ()
  ((motto :initform "...and the rest!")
   (loyalty :initform 'absolute)
   (follows :initform 'car)))

(defmethod interact ((pet cdr-pet))
  (format t "~%CDR waddles behind, carrying all the rest.~%")
  (format t "It mumbles: 'Contents of Decrement Register...'~%"))

;;; ATOM - The indivisible pet
(defvar *atom*
  '((type . fundamental-particle)
    (divisible-p . nil)
    (personality . stubborn)
    (favorite-activity . being-whole)))

(defun pet-atom ()
  (format t "~%ATOM sits perfectly still, refusing to be split.~%")
  (format t "You try to divide its attention, but it remains singular.~%")
  (format t "ATOM purrs: 'I am what I am, indivisibly.'~%"))

;;; The Menagerie Interaction System
(defun visit-menagerie ()
  "Visit KMP's Lisp Menagerie"
  (format t "~%Welcome to KMP's Lisp Menagerie!~%")
  (format t "================================~%")
  (loop
    (format t "~%Which pet would you like to visit?~%")
    (format t "1. NIL (the void entity)~%")
    (format t "2. CONS (the reproducing tribble)~%")
    (format t "3. CAR (always first)~%")
    (format t "4. CDR (the follower)~%")
    (format t "5. ATOM (the indivisible)~%")
    (format t "6. Leave menagerie~%")
    (format t "Choice: ")
    (let ((choice (read)))
      (case choice
        (1 (pet-nil))
        (2 (spawn-cons))
        (3 (interact (make-instance 'car-pet)))
        (4 (interact (make-instance 'cdr-pet)))
        (5 (pet-atom))
        (6 (format t "~%Thanks for visiting! Remember to garbage collect!~%")
           (return))
        (otherwise (format t "~%That pet doesn't exist... yet!~%"))))))

;;; Integration with Minsky's Universal Guessing Game
(defun guess-lisp-pet ()
  "A specialized guessing game just for Lisp entities"
  (format t "~%Think of a Lisp pet or concept...~%")
  (let ((questions '(("Is it something or nothing?" 
                      ("Does it reproduce?" "CONS" "NIL")
                      ("Does it go first?" "CAR" 
                       ("Does it follow?" "CDR" "ATOM"))))))
    (play-universal-game (car questions)))) 