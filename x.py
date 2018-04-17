
class FamilyFeud:

    def buzzer(self, height, char='X'):

        char_pos = 0
        for row_num in range(0, height):

            line = []
            for col_num in range(0, height):
                # Always print entire first and last row
                if row_num in [0, height - 1]:
                    line.append(char)
                # Always print entire first and last column
                elif col_num in [0, height - 1]:
                    line.append(char)
                # Print char at current and opposite position marker
                elif col_num in [char_pos, height - char_pos - 1]:
                    line.append(char)
                # No dice
                else:
                    line.append(' ')

            print(''.join(line))
            char_pos += 1


feud = FamilyFeud()
feud.buzzer(10)
