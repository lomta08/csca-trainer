import { Route, Routes, Link } from 'react-router-dom';
import { Layout } from './components/Layout';
import { Home } from './pages/Home';
import { LearnIndex } from './pages/LearnIndex';
import { Lesson } from './pages/Lesson';
import { Formulas } from './pages/Formulas';
import { Practice } from './pages/Practice';
import { Drill } from './pages/Drill';
import { MockHome } from './pages/MockHome';
import { MockRun } from './pages/MockRun';
import { MockResult } from './pages/MockResult';
import { Mistakes } from './pages/Mistakes';
import { Plan } from './pages/Plan';
import { Tutor } from './pages/Tutor';
import { Resources } from './pages/Resources';
import { ChemData } from './pages/ChemData';
import { Chinese } from './pages/Chinese';
import { Settings } from './pages/Settings';

export function App() {
  return (
    <Layout>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/learn" element={<LearnIndex />} />
        <Route path="/learn/:subject/:subtopic" element={<Lesson />} />
        <Route path="/formulas" element={<Formulas />} />
        <Route path="/formulas/:subject" element={<Formulas />} />
        <Route path="/practice" element={<Practice />} />
        <Route path="/drill" element={<Drill />} />
        <Route path="/mock" element={<MockHome />} />
        <Route path="/mock/run" element={<MockRun />} />
        <Route path="/mock/result/:id" element={<MockResult />} />
        <Route path="/mistakes" element={<Mistakes />} />
        <Route path="/plan" element={<Plan />} />
        <Route path="/tutor" element={<Tutor />} />
        <Route path="/resources" element={<Resources />} />
        <Route path="/chemistry-data" element={<ChemData />} />
        <Route path="/chinese" element={<Chinese />} />
        <Route path="/settings" element={<Settings />} />
        <Route
          path="*"
          element={
            <div className="card">
              <h1>Page not found</h1>
              <Link to="/">Back to the dashboard</Link>
            </div>
          }
        />
      </Routes>
    </Layout>
  );
}
