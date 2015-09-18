from sys import argv

script, filename = argv

txt = open(filename)

print 'Thats your file: %r' % filename
print txt.read()

txt.close()