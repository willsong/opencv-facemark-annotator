import os
import shutil
import sys

max_images = 100

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: annotate.py <original-path> <target-path>')
        sys.exit(0)

    origPath = sys.argv[1]
    targetPath = sys.argv[2]

    imageList = []
    annotList = []

    entries = os.listdir(origPath)
    cnt = 0
    for fname in entries:
        fullPath = os.path.join(origPath, fname)
        imgName = fname[:-4]
        imgPath = os.path.join(origPath, imgName)
        if fname.endswith('cat') and os.path.isfile(imgPath):
            with open(fullPath) as fh:
                content = fh.read()

            output = '''version: 1
n_points: 9
{{
{0}
{1}
{2}
{3}
{4}
{5}
{6}
{7}
{8}
}}
'''

            # trim first 2 chars
            content = content[2:].strip()

            # get pairs of numbers
            toks = content.split(' ')
            if len(toks) != 18:
                print('Not enough pairs of numbers: {}'.format(toks))
                continue

            output = output.format(toks[0] + ' ' + toks[1], toks[2] + ' ' + toks[3], toks[4] + ' ' + toks[5], toks[6] + ' ' + toks[7],
                    toks[8] + ' ' + toks[9], toks[10] + ' ' + toks[11], toks[12] + ' ' + toks[13], toks[14] + ' ' + toks[15], toks[16] + ' ' + toks[17]).strip()

            annotPath = os.path.join(targetPath, imgName + '.txt')
            newImgPath = os.path.join(targetPath, imgName)
            if os.path.isfile(annotPath):
                print('File already exists, skip: {}'.format(annotPath))
                continue
            if os.path.isfile(newImgPath):
                print('File already exists, skip: {}'.format(newImgPath))
                continue
            shutil.copyfile(imgPath, newImgPath)
            with open(annotPath, 'w') as fh:
                fh.write(output)
            print('Copied {0} to {1} and annoated in {2}'.format(imgPath, newImgPath, annotPath))

            imageList.append(newImgPath)
            annotList.append(annotPath)

            cnt += 1
            if cnt > max_images:
                print('Reached image limit of {0}'.format(max_images))
                break

    annotFile = os.path.join(targetPath, 'annot.txt')
    with open(annotFile, 'a') as fh:
        fh.write("\n".join(annotList) + "\n")

    imageFile = os.path.join(targetPath, 'images.txt')
    with open(imageFile, 'a') as fh:
        fh.write("\n".join(imageList) + "\n")

    print('Done')
