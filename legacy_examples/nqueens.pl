use strict;
use warnings;

sub isSafe {
    my ($board, $row, $col, $N) = @_;

    # Check for queens in the same column
    for (my $i = 0; $i < $row; ++$i) {
        if ($board->[$i][$col] eq 'Q') {
            return 0;
        }
    }

    # Check upper left diagonal
    for (my $i = $row, my $j = $col; $i >= 0 && $j >= 0; --$i, --$j) {
        if ($board->[$i][$j] eq 'Q') {
            return 0;
        }
    }

    # Check upper right diagonal
    for (my $i = $row, my $j = $col; $i >= 0 && $j < $N; --$i, ++$j) {
        if ($board->[$i][$j] eq 'Q') {
            return 0;
        }
    }

    return 1;
}

sub solveNQueens {
    my ($board, $row, $N) = @_;

    if ($row == $N) {
        # Print the solution
        for (my $i = 0; $i < $N; ++$i) {
            for (my $j = 0; $j < $N; ++$j) {
                print $board->[$i][$j] . ' ';
            }
            print "\n";
        }
        print "\n";
        return;
    }

    for (my $col = 0; $col < $N; ++$col) {
        if (isSafe($board, $row, $col, $N)) {
            $board->[$row][$col] = 'Q';
            solveNQueens($board, $row + 1, $N);
            $board->[$row][$col] = '*';  # Backtrack
        }
    }
}

sub printNQueens {
    my ($N) = @_;

    my @board;
    for (my $i = 0; $i < $N; ++$i) {
        push @board, [('*') x $N];
    }

    solveNQueens(\@board, 0, $N);
}

print "Enter the size of the chessboard (N): ";
my $N = <STDIN>;
chomp $N;

printNQueens($N);

exit 0;
