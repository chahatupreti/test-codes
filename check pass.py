def fm(gsl):
	for i in xrange(100):
		d=0
		s=''
		#print 5
		for a in gsl: 
			d=d+1
			#print d, len(gsl)
			print d*100/len(gsl), '%'
			total = 0.0
			for i in range(99): # xrange is slower according 
			    for j in range(1, 99):            #to my test but more memory-friendly.
			        total += (i / j)
			#print total
			if not(a=='4'):
			    #print 'erere'
			    s += a
			    dd=d*d*d
			    ee=d*d*d*d
			    #print s,dd,ee
	        #return d
	
	
gsl = ['aaa', 'aaat', 'aat', 'acg', 'ai', 'aldr', 'ana', 'asy', 'acc', 'ack', 'aga', 'agat', 'agc', 'ald', 'alr', 'app', 'ar', 'bi', 'bel', 'bri', 'cas', 'cct', 'ce', 'chn', 'cr', 'car', 'caga', 'cal', 'carr', 'cctg', 'cel', 'cg', 'cgt', 'cistr', 'ck', 'cle', 'clo', 'cm', 'comp', 'con', 'cor', 'crip', 'cript', 'cs', 'dat', 'den', 'des', 'ei', 'el', 'emp', 'ep', 'erm', 'ecto', 'ell', 'em', 'enc', 'ende', 'eo', 'era', 'erf', 'fp', 'fr', 'fam', 'fir', 'flo', 'gat', 'ggt', 'gr', 'gaa', 'gatc', 'gca', 'gcat', 'gcc', 'gct', 'gctg', 'ggc', 'ggct', 'gma', 'hip', 'hy', 'ip', 'ipt', 'irs', 'ic', 'ica', 'icat', 'id', 'ide', 'ie', 'ig', 'igg', 'igm', 'im', 'ka', 'ki', 'kit', 'lec', 'lon', 'lar', 'lat', 'll', 'lok', 'lyz', 'mis', 'mal', 'ment', 'met', 'ml', 'mp', 'mpl', 'myc', 'ne', 'nn', 'nne', 'nom', 'nst', 'nt', 'nan', 'nat', 'nano', 'nes', 'ng', 'nical', 'nin', 'nts', 'numb', 'oc', 'og', 'ot', 'odin', 'om', 'omi', 'omp', 'opr', 'os', 'osi', 'pa', 'pc', 'pe', 'pl', 'pp', 'ppr', 'pr', 'prot', 'pen', 'perf', 'peri', 'pli', 'po', 'pon', 'poo', 'ppl', 'pres', 'ps', 'pt', 'pts', 'rc', 'rd', 'rea', 'ra', 'rac', 'ral', 'ray', 'ren', 'rf', 'ri', 'ric', 'rim', 'rip', 'rn', 'ro', 'rob', 'ron', 'rop', 'rst', 'se', 'sec', 'ser', 'si', 'sse', 'st', 'sa', 'san', 'scr', 'sele', 'sig', 'sin', 'sor', 'str', 'tec', 'ter', 'tgc', 'tl', 'tr', 'tag', 'tal', 'tc', 'tcta', 'tes', 'tif', 'trac', 'tro', 'ts', 'ty', 'uce', 'uti', 'ul', 'um', 'va', 'vav', 've', 'vec', 'whi', 'wo', 'xt', 'ym', 'ab', 'ag', 'aly', 'ang', 'ap', 'ba', 'bre', 'bs', 'cga', 'ci', 'cla', 'cod', 'cri', 'cripto', 'crn', 'cy', 'da', 'de', 'dep', 'din', 'ding', 'dr', 'du', 'dy', 'ent', 'ermin', 'fa', 'fi', 'ft', 'fy', 'gag', 'gc', 'ge', 'gro', 'gt', 'ha', 'hes', 'hn', 'kd', 'la', 'ld', 'le', 'lu', 'med', 'mes', 'mic', 'mr', 'nc', 'nd', 'ni', 'ol', 'op', 'oto', 'par', 'ple', 'pol', 'pu', 'rol', 'rs', 'ru', 'samp', 'sb', 'sc', 'sti', 'su', 'sy', 'ttg', 'tct', 'te', 'th', 'ti', 'tor', 'tu', 'tw', 'typ', 'ub', 'ur', 'wh', 'wi', 'wil', 'wn', 'av2', 'ccm3', 'm3', 'm33', 'th', 'vav2', 'vav3']
a=fm(gsl)
#print a