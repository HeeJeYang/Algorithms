import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        String breads = sc.next();
        LinkedList<Character> l = new LinkedList<>();

        for (int i = 0; i < breads.length(); i++) {
            l.add(breads.charAt(i));
        }

        // for (int i = 0; i < l.size(); i++) {
        //     System.out.println(l.get(i));
        // }

        ListIterator<Character> it = l.listIterator(l.size());

        for (int i = 0; i < m; i++) {
            char command = sc.next().charAt(0);
            // System.out.println("command is" + " " + command);
            switch (command) {
                case 'R':
                    if (it.hasNext()) {
                        it.next();
                    }
                    break;
                case 'L':
                    if (it.hasPrevious()) {
                        it.previous();
                    }
                    break;
                case 'D':
                    if (it.hasNext()) {
                        it.next();
                        it.remove();
                    }
                    break;
                case 'P':
                    char c = sc.next().charAt(0);
                    it.add(c);
            }
        }

        it = l.listIterator();
        while (it.hasNext()) {
            System.out.print(it.next());
        }
        System.out.println();
    }
}