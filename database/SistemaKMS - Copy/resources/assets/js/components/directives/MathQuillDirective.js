//import MathQuill from 'mathquill';
//import './mathquill/mathquill.css'; // Importa el archivo CSS de MathQuill
//import MathQuill from './mathquill';
//import MathQuill from 'mathquill';
import '@/components/mathquill/mathquill.css';

// Importa el archivo JS de MathQuill desde la carpeta local
import MathQuill from '@/components/mathquill/mathquill.js';
export default {
 created() {
    
  },
  bind(el) {
    const MQ = MathQuill.getInterface(2);
    const mathField = MQ.MathField(el, {
      handlers: {
        edit: () => {
          el.dispatchEvent(new Event('input', { bubbles: true }));
        },
      },
    });
    el.__mathField__ = mathField;
  },
  unbind(el) {
    if (el.__mathField__) {
      el.__mathField__.dispose();
      delete el.__mathField__;
    }
  },
};
