class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        Central idea: push right-moving asteroids onto the stack,
        Left-moving asteroids are compared against the stack's top.

        Invariant: The stack will be prefixed with left-moving (negative)
                   asteroids and suffixed with right-moving.
        """
        
        # Initialise to the first asteroid
        stack = [asteroids[0]]
        
        for asteroid in asteroids[1:]:
            if asteroid > 0:  # Right-moving (asteroid is >0)
                stack.append(asteroid)
            else:  # Left-moving (asteroid is <0; asteroids[i] is never 0)
                """
                Continually evaluate how many right-moving asteroids
                the incoming left-moving one will destroy, until the
                left-moving one itself is destroyed or the stack is
                empty.
                """
                should_append = True

                while stack:
                    if stack[-1] < 0:
                        break
                    elif stack[-1] + asteroid == 0:
                        # "If both are the same size, both will explode"
                        stack.pop()
                        should_append = False
                        break
                    elif stack[-1] + asteroid > 0:
                        # Right-moving destroyed the incoming asteroid
                        should_append = False
                        break
                    elif stack[-1] + asteroid < 0:
                        # Left-moving destroys the immediate astroid
                        stack.pop()
                
                if should_append:
                    stack.append(asteroid)

        return stack

                