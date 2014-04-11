


import urllib2
from bs4 import BeautifulSoup

response = urllib2.urlopen('http://simple.wikipedia.org/wiki/Cat')
html = response.read()
soup = BeautifulSoup(html)
text =  soup.get_text()
print text[0:10000]


cats1 = """
Cats, also called domestic cats or house cats (Felis catus), are carnivorous (meat-eating) mammals, of the family Felidae.
Cats have been domesticated (tame) for nearly 10,000 years.[1] They are currently the most popular pets in the world.[2] Their origin is probably the African Wildcat Felis silvestris lybica.
Cats were probably first kept because they ate mice, and this is still their main 'job' in farms throughout the world. Later they were kept because they are friendly and good companions.
A young cat is called a kitten. Cats are sometimes called kitty or pussycat. An entire female cat is a queen, and an entire male cat is a tom.[3]
Domestic cats are found in shorthair and longhair breeds. Cats which are not specific breeds can be referred to as 'domestic shorthair' (DSH) or 'domestic longhair' (DLH).
The word 'cat' is also used for other felines. Felines are usually classed as either big cats or small cats. The big cats are well known: lions, tigers, leopards, jaguars, pumas, and cheetahs. There are small cats in most parts of the world, such as the lynx in northern Europe. The big cats and wild cats are not tame, and can be very dangerous.

Past range of Felis sylvestris.


In the past, people kept cats because the cats hunted and ate mice, rats, and insects. The oldest evidence of cats kept as pets is from the Mediterranean island of Cyprus, around 7500 BC.
Ancient Egyptians worshipped cats as gods, and often mummified them so they could be with their owners "for all of eternity". (They also mummified mice so the cats would have something to eat in the afterlife.) Today, people often keep cats as pets, but there are also cats that live without being cared for by people. These kinds of cats are called "feral cats".
Today, special food for cats is widely available in the developed countries. Proper feeding will make a cat live much longer compared to hunting or being fed table scraps. Not correctly feeding a cat can lead to problems (see below for health concerns).
Cats cannot taste sweet foods (with sugar) because of a mutation (change) in their ancestors which removed the ability to taste sweet things.
Cat anatomy[change | edit source]
Cats have anatomy similar to the other members of the genus Felis. The genus has extra lumbar (lower back) and thoracic (chest) vertebrae. This helps to explain the cat's spinal mobility and flexibility. Unlike human arms, cat forelimbs are attached to the shoulder by free-floating clavicle bones. These allow cats to pass their body through any space into which they can fit their heads.[4]
The cat skull is unusual among mammals in having very large eye sockets and a powerful and specialized jaw.[5]:35 Compared to other felines, domestic cats have narrowly spaced canine teeth: this is an adaptation to their preferred prey of small rodents.[6] Cats, like dogs, walk directly on their toes, with the bones of their feet making up the lower part of the visible leg.[7]
Cats walk very precisely. Unlike most mammals, when cats walk, they use a "pacing" gait; that is, they move the two legs on one side of the body before the legs on the other side. This trait is shared with camels and giraffes. As a walk speeds up into a trot, a cat's gait will change to be a "diagonal" gait, similar to that of most other mammals: the diagonally opposite hind and forelegs will move at the same time.[8] Most cats have five claws on their front paws, and four on their rear paws.[9] On the inside of the front paws there is something which looks like a sixth "finger". This special feature, on the inside of the wrists, is the carpal pad, also found on other cats and on dogs.
Behaviour[change | edit source]




The cat on the right is fed up with the cat on the left and this is a semi-serious warning.






The stripes on this standard tabby cat help it hide in long grass and bushes. It's a kind of camouflage.


Cats are active carnivores,[10] meaning they hunt live prey. Their main prey is small mammals (like mice). They will also stalk, and sometimes kill and eat, birds. Cats eat a wide variety of prey, including insects, and seem especially to like house flies and bluebottles. Their main method of hunting is stalk and pounce. Wh


"""
cats2 = """ """

#print html[0:1000]

